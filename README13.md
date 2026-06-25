# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aacb7d8b-0c0e-3624-9f32-100468ccddce | -11.88014 | -51.75819 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77cd066f-0722-35a8-b445-558c2c3acf0f | -8.67635 | -47.86323 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4f418d2c-aa20-3e10-8718-6ac39ae31881 | -11.91254 | -43.40295 | 2026-06-25 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5d0ef07-e16d-3e02-8fe8-0506b0d1f2b8 | -9.09408 | -47.5274 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e478005c-46d8-3371-88ec-4b554cfcd3e5 | -8.68742 | -47.86096 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 18f126e3-9060-3a5f-9afd-17154b89ff63 | -11.89448 | -51.74566 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1da4a734-d19a-34b4-897e-86b99ae0a88d | -11.7901 | -56.99463 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda438dd-abb7-3c34-b753-8887a71a55c7 | -9.09468 | -47.52335 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32f7233c-7baf-3c1b-ad46-ea66b6004ee3 | -12.745 | -44.46676 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b39f681-4b22-3d75-9d12-21346099c5e8 | -9.45986 | -49.83016 | 2026-06-25 04:49:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cebc55ea-2afa-3dc6-8a96-3c6e1781c7f2 | -11.8701 | -51.75652 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84aa755-fe15-3869-8ab5-2dc7264d970d | -11.64104 | -52.86092 | 2026-06-25 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 036b331f-dfad-3bde-8d77-0a55ede04d6a | -11.87852 | -51.74689 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52fc184b-cd41-3847-991f-f727affba56f | -12.74724 | -44.46471 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f91f443d-7e1c-3426-8e42-6b30e2cf07fb | -10.38871 | -56.76492 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2187732-427e-3e3a-a402-65fabd1f6ef6 | -10.36693 | -47.34183 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7815b6-6035-30be-bc55-5e14a2f19e6c | -10.36993 | -47.34662 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dafcb3c5-1cca-3d81-a39a-2bacdd9cde25 | -11.87287 | -51.76066 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| cf9fc847-340c-38ef-8684-888e80110562 | -10.37421 | -47.34291 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c54e44c3-950b-37e3-bd83-fd5b12a366c4 | -8.41581 | -46.88276 | 2026-06-25 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7be370-a773-31e6-9e03-6a059496cede | -11.87737 | -51.75405 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 18e2d278-b8e6-388a-ab7f-182b8610dfda | -11.88072 | -51.7546 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 8d2d2578-2267-3408-8ac0-bbdb1f462704 | -6.98091 | -42.8929 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 38562cb1-283a-3fa8-9254-7f5dcd98652c | -10.61495 | -47.17376 | 2026-06-25 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34a35aa-d730-3d3a-b021-90f75920b60a | -7.0006 | -42.78238 | 2026-06-25 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77c1bd90-8aad-309f-b7db-8fec323b0a60 | -12.75073 | -44.45832 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d8c6ef4-5ad6-3f6b-8ccb-e481a39a53f9 | -9.88328 | -52.43781 | 2026-06-25 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd91c337-3b9b-3e8b-843b-35287030b4a6 | -6.36633 | -47.379 | 2026-06-25 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3beff254-f66b-3edb-a019-a19494a087c1 | -7.7563 | -44.61934 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 14124bc6-84b2-3e4f-b8f5-a9e094f3ddb6 | -9.53131 | -47.75754 | 2026-06-25 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d9aa22-13eb-391d-82cd-6ae794014ba7 | -6.99855 | -42.77383 | 2026-06-25 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7e43b72-fb63-3e75-bda4-7ad85208d484 | -9.77268 | -48.25639 | 2026-06-25 04:49:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0880d837-4f45-32fd-a1aa-c44433f27887 | -9.7436 | -47.87756 | 2026-06-25 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fabddfa-0d76-37f6-9aa0-31f147ba0caf | -10.41383 | -46.73782 | 2026-06-25 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49b3873f-a6d4-3b59-9229-f36b41769a18 | -6.99731 | -42.77213 | 2026-06-25 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 216be44f-94be-3eee-a43b-518f29cfdeae | -12.06542 | -48.42295 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c78749-bcef-3f98-b40b-3c41dbbe9b17 | -11.79946 | -56.99204 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9286911-ac02-3902-85f8-46592b686857 | -12.74623 | -44.4577 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b13cab3d-bbaf-31c8-931e-7cb2bc21f625 | -12.31454 | -46.73673 | 2026-06-25 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdaf28a0-7913-37d7-a420-ea8cdd53391a | -7.74445 | -44.61369 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5030c587-85fb-3752-8db4-32db8522854a | -11.8746 | -51.74991 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 4ef5b92e-a2fb-3b6e-8f59-d7d0520e2d79 | -10.42069 | -46.74349 | 2026-06-25 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdc90e0f-8d22-35a2-a93b-8ac62f3f99bc | -9.58116 | -49.12015 | 2026-06-25 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06227494-6059-3af9-8c79-f44ff5c04dfd | -10.77301 | -54.11003 | 2026-06-25 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed9f445-dfcb-3470-8593-4b2432669594 | -11.79441 | -56.9954 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66242478-2192-35c8-b9e7-2e94fff16ceb | -11.35855 | -55.82185 | 2026-06-25 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3953283-14fe-3f17-9d9d-131e5477914a | -7.73538 | -44.17758 | 2026-06-25 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f087f9af-7936-3b31-9dc7-4e9e48c093d4 | -10.38357 | -56.71278 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a266efa-b591-3b57-8f40-12aa3ffe7fdc | -11.90776 | -43.4023 | 2026-06-25 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aef71d4-d8f4-3e24-b279-2022c2af924d | -11.50281 | -54.50233 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2000dc6b-8a61-3252-907d-191b3ee6cdc3 | -11.8919 | -51.74911 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3226b43-a680-39c3-a0f8-8a5b8ec19107 | -11.31986 | -43.32938 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87256947-1d15-31c6-8947-00f973b5d515 | -11.89248 | -51.74554 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7f99b56-7839-3d45-b196-0f247c7deb1d | -11.88856 | -51.74855 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 062989bf-cdc9-30e5-9d93-657b9adc2de0 | -9.36412 | -50.54372 | 2026-06-25 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56670552-b6da-3b77-9bf5-83199cd42dda | -10.77594 | -54.11501 | 2026-06-25 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee32bf6d-9b8c-3f9f-9ff9-0cc0d6c2afd5 | -6.97531 | -42.89553 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6508d2eb-3c7a-391c-a7b6-e92449170a77 | -11.58566 | -47.44416 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e31f303-3d14-33d6-834c-3f6474bef3ba | -11.9197 | -44.17179 | 2026-06-25 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f950528e-20d8-3b83-8194-a6a24844b5a0 | -11.19996 | -49.41477 | 2026-06-25 04:49:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a107a58-f5ae-382e-998d-2588647bfa82 | -7.74033 | -44.61298 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63ede992-80b7-3b71-9485-4e2e5657548e | -9.19723 | -45.3219 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7f6f790-ca5a-3773-bc7a-50aaa78a4cbf | -9.19637 | -45.32199 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5abc7f9-2694-3b8b-ae5a-d4acee82f2fd | -8.85463 | -46.93398 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed60b095-eeb1-3fb8-81f1-e921aab6e73e | -11.87622 | -51.76122 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ce582a45-d4ef-357f-a409-79c4e4c34351 | -10.12582 | -52.1095 | 2026-06-25 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef5ecec9-0642-32cd-9e43-b0c0772a3d79 | -7.73054 | -44.18093 | 2026-06-25 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abe6ada-0b1d-33c5-805b-2e53612a23ca | -12.83055 | -44.35495 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 355fe2de-a10d-39a4-8871-6ed46ab16276 | -8.12792 | -47.89251 | 2026-06-25 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e6a7c8-7d5e-30e5-9f2b-a1dd0b9f8325 | -11.24714 | -43.3302 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| abd05be4-7182-344e-a84d-266b0cb89eff | -12.08015 | -54.61581 | 2026-06-25 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 590694b9-c89b-36dd-91c9-e8d2b3a1be36 | -11.91184 | -43.40816 | 2026-06-25 04:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87936872-ff00-3343-a4e1-dfa82bcce937 | -9.20933 | -45.32367 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec0de555-ae72-3929-9ea3-2eb0223e92d6 | -9.07133 | -44.74635 | 2026-06-25 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e600fada-ec13-3b39-95e0-c0c7b6e7b644 | -11.58996 | -47.44034 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8515690d-4b6f-3f7a-818b-365bdc31230f | -8.85825 | -46.93467 | 2026-06-25 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6e09d56-13de-3ca8-a2b6-80a6af025cda | -9.21286 | -45.32781 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6115063-a3b3-38bc-83b3-b4330a8e72c4 | -12.74051 | -44.46614 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c7eb3c75-3e85-3052-bec3-ba4f534bbc5d | -7.74227 | -44.62864 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 577b29ec-41f9-3c23-ac0d-1f8ded4a09a5 | -11.50357 | -54.49788 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ef6a6d-f8c9-370b-b0ab-c4df5251c34f | -7.80602 | -46.46148 | 2026-06-25 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4d88cae-cb8f-3188-9dad-f399e84941bc | -11.32052 | -43.32431 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3c74eda-f446-3a50-9be1-0f29a95444f8 | -9.07187 | -44.74247 | 2026-06-25 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11718685-4da1-36b1-8a1b-1cd29f0dbf3f | -7.74391 | -44.61741 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 703eeaeb-4b49-3218-9c67-76eec2ce15de | -9.07031 | -44.74628 | 2026-06-25 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75fb46a0-3f83-39d3-85e5-e21c68341f3c | -6.98912 | -42.89746 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 21d9802c-d1ef-3d9d-8187-9bd77e69e7ea | -10.39346 | -56.75861 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d7836c8-5efb-32fd-b1a8-a60fcd8d47b7 | -13.20159 | -48.32246 | 2026-06-25 04:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a1a99cd-207c-3092-9ceb-86cb86a11b44 | -9.10428 | -47.45856 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51269f22-3621-34e9-be34-de30b2c55560 | -7.80667 | -46.45717 | 2026-06-25 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6ae5ab6-2b22-3864-b9c4-4d7d710a9da4 | -11.78915 | -57.35004 | 2026-06-25 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c9468d3-9ab4-3265-b11e-b66ad41b2911 | -10.39199 | -56.76704 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac72f697-3171-348f-a101-49d51a7ddf07 | -9.74832 | -47.87021 | 2026-06-25 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e6e6855-4595-32f6-add8-3bc430c97add | -9.88266 | -52.44158 | 2026-06-25 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e439320-6f95-3f29-8c6d-88b621ef4ac4 | -11.88129 | -51.75102 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 6fea40c7-b385-3303-8cab-604e86130e0d | -8.85367 | -46.93612 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c35d380-a974-30fc-bd96-d5930ac7b60c | -9.53191 | -47.75354 | 2026-06-25 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c96c991-acc4-3d9d-9ad7-7465cda9828a | -12.31384 | -46.74155 | 2026-06-25 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50645756-cd38-3593-a5ae-b402c0b27c87 | -6.50537 | -42.2238 | 2026-06-25 04:49:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab618331-3c2f-3604-ab28-7a5fda8cfea3 | -9.98096 | -47.73582 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
