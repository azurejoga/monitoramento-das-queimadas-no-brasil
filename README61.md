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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4103cf22-492f-3135-8bf5-c254e0f57bca | -7.88077 | -47.24929 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be6e384f-c901-31a9-9542-5b68b119298e | -6.88401 | -45.15335 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3239020-d78b-3be5-a324-3338e7e33e31 | -9.13242 | -45.8631 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3476ed1a-bc87-3842-a117-4892d5dff1e9 | -10.53724 | -49.79726 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf8ab6b8-dccf-39fe-a4ba-1c8bdd26a49e | -10.34343 | -54.19987 | 2025-10-27 05:01:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7cda365-6256-365a-9f11-25f362bc7750 | -7.2361 | -44.98705 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2ae6135-accd-32de-8ec1-31a070ec52d0 | -7.78148 | -45.38077 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c362437-18aa-375b-8f3c-227af7bc9939 | -7.85425 | -46.46892 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 804324c9-eff6-38d0-9e5f-45dfa4f9c870 | -12.32093 | -47.48879 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb057a47-c3b8-39cf-b2b8-50cb2e81a292 | -10.75069 | -44.20073 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| deefaab7-bbe1-3e19-9c43-19463521e25d | -11.33059 | -53.92678 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9a815cc-8fd4-336b-adac-fb8544268bc4 | -8.32255 | -46.83089 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae80d60e-f566-3945-8e3c-af61aa252762 | -11.0218 | -47.80475 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b15560-0132-33bb-989b-beba0626d197 | -11.62712 | -54.5801 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a4990be-f83e-3daf-ba16-77eacf28a40a | -10.90241 | -50.23347 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93ff0046-29b0-3ab9-ab02-5a071afecc14 | -10.3146 | -47.18191 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a560a21-978d-3184-8618-f59a8065a021 | -7.06415 | -46.75951 | 2025-10-27 05:01:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df5e4c4b-5f89-35a6-8a59-a1b44e33bf38 | -11.06216 | -50.35765 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3428de70-8fa0-3b8a-bbe7-94339755c646 | -9.13335 | -45.85629 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e00d4c55-4448-36ee-9f16-c142383fc5d7 | -9.23091 | -45.84554 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3604436b-56fd-352b-b04d-f23372d60d22 | -10.56522 | -47.88557 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2b537e9-a713-357b-883e-78df3a354654 | -9.13628 | -51.30549 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a4374535-ad32-3670-9471-e4830a34bce6 | -9.88455 | -58.03243 | 2025-10-27 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd61ca3a-add0-3ba6-919f-4a777de66f25 | -7.76895 | -45.39231 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 275dd123-5900-3f9c-b9ce-3d8d1b0469a0 | -10.57957 | -47.99509 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f45fef2-fdb8-3f21-911d-3e1b46d273a6 | -10.95436 | -49.81234 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e094347-bd07-3ea8-99f2-724ae2b87bff | -9.58845 | -44.94803 | 2025-10-27 05:01:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62482d3b-f1b4-31c8-81af-74f2280acab9 | -9.45128 | -56.6443 | 2025-10-27 05:01:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 112fa32e-b400-31bc-9663-7f42e6445bec | -7.83845 | -46.47268 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1744a94-8c81-3f74-bb0d-50f21724440c | -5.71842 | -49.28486 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f02ca752-f35c-3a32-9133-5ee7d4aa4da2 | -9.58101 | -45.1862 | 2025-10-27 05:01:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 536e41d9-da37-3e79-bf30-040d9493a0ea | -6.14887 | -43.13413 | 2025-10-27 05:01:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e7fb678-656b-3dce-b150-e0dca37c955b | -12.04917 | -46.38107 | 2025-10-27 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5abaf00-4df4-3383-85cc-ac183f24c9b9 | -10.31237 | -47.1985 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| debe9772-e6e0-3874-a8ab-f614eb4cd7fc | -7.33516 | -47.14573 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 46e3c35c-b8fc-356d-98c0-ff312cdcb55c | -9.26943 | -45.6012 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090e2554-7255-34a0-8af3-2f8ed3f49fce | -10.17115 | -49.31184 | 2025-10-27 05:01:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab1e5c85-2e3f-3e19-8d31-a6cd4d6ab08a | -9.84441 | -52.27137 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72af583-79af-3a8b-ab1e-e3748dbd244d | -7.8633 | -45.71346 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f2c26d0-baa7-36de-bfed-6e4e0ba086cb | -7.77434 | -45.39294 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d0caa92b-f54b-3a5e-bf79-61f7ac6f4ca4 | -10.31654 | -47.20475 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b07d8fa-d559-3154-8872-c93f2667232a | -7.82885 | -46.4316 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c060348-6657-3424-aa59-a053a3c62f0b | -7.81434 | -45.39603 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b6d22a5-c125-3a3f-acfb-0e794e4b9762 | -8.529 | -45.56262 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c108899-5537-36c8-a42f-ac8d701915bb | -8.71827 | -49.40416 | 2025-10-27 05:01:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f29d7c3f-4989-3204-9d26-c3012f229bd2 | -7.84548 | -46.42215 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07de96f5-9bd8-3393-bdaf-32e73aeeb10c | -7.43681 | -41.87271 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d9b1f0ae-7f84-306f-9004-02f6ae9be32f | -12.34379 | -47.11361 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00f10134-ea5a-3c62-a106-c8733596f377 | -8.3614 | -46.15729 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9d06e53-a678-3246-b96a-fabd5240c533 | -7.60067 | -45.68359 | 2025-10-27 05:01:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2de57c77-0953-3e6d-9003-38e83bb6710d | -8.73794 | -49.60506 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99d3ead-e4ac-35fe-83ba-fc49813f5242 | -7.88548 | -47.25013 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60f94b66-0296-3e87-ac1a-cf01db2d5c96 | -8.01232 | -47.38292 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6525c628-7d73-3062-b065-b1fdd1f27e62 | -11.43786 | -54.09293 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 943d28e0-fe65-3bde-a1f7-f4da6689b391 | -8.9626 | -47.18884 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 91048e6f-f8bd-3b77-bb45-f13e69ac5ac9 | -7.76937 | -45.38925 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ebefee1-9dbb-3aab-a55e-8b21ed3b61e2 | -10.35951 | -47.19027 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| a22f77f3-5e5c-3a4a-84bf-835ba5c9aeff | -10.21331 | -52.662 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9417f150-9c3b-38a3-abb8-3a10909666ae | -6.64012 | -44.63293 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8fbbfbe-ccd8-3967-801c-13caec7f69dc | -7.82842 | -46.47157 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97eb65b7-a82a-326b-a835-8a9483c8ef8d | -9.13107 | -45.86452 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16c6a370-b9ee-3131-8ba1-b38ea8240393 | -7.76312 | -45.39494 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24230e19-b881-3c9c-902b-30180ad6cc52 | -10.87989 | -54.04742 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71bff13-a65f-3d77-a7c3-d12fba2e6a4f | -9.99002 | -47.17336 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efb72cc4-4168-33b8-84e6-3a7a2d8cae5e | -10.57214 | -48.01532 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 374092e2-499f-3c72-b152-5575d7c2e2ef | -10.95326 | -47.58507 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5926b2ff-831f-3284-a80e-0a9c2041d085 | -10.68632 | -47.84618 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d99148e-13ba-3343-aeff-3a8bdb5cedac | -12.52571 | -49.59194 | 2025-10-27 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ad18709-1d03-397d-88d3-b57b33d43340 | -7.82228 | -46.44224 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 231d2a6c-30ed-3b70-abc8-146c6c947572 | -10.5863 | -47.86102 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0104ab3-a738-3358-83eb-4a2285f85310 | -7.42944 | -41.87714 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7f0629d5-1ca2-3b6d-b38c-8ca11de4d9de | -10.03273 | -47.16838 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c34fc863-4967-31dc-abed-88724ad67251 | -12.33228 | -47.47932 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 463fc519-8b87-3f20-b5c0-635700406ddf | -11.91674 | -43.82386 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbb8de8e-164a-3606-8e12-524f1f4755cd | -10.356 | -47.17858 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 64998698-6afa-3946-a9f5-4249ab200057 | -6.14951 | -43.12947 | 2025-10-27 05:01:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 821fc18a-5ee6-3ba9-a22e-e369310d7195 | -6.38003 | -44.26845 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78d6869b-8f16-307b-9cb2-f2f418ed2e8a | -10.068 | -48.20436 | 2025-10-27 05:01:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d85c05a-b3f8-3793-8380-3b06d8b2e1cd | -8.87747 | -44.84123 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7961aec-2e8e-30ba-a2df-bab8e73fa2db | -7.35906 | -50.43167 | 2025-10-27 05:01:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbb260fe-e433-335a-b040-e917c3b7cd68 | -7.24504 | -46.95714 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df70c7f8-568d-383d-a651-699f672eb277 | -6.17649 | -49.87298 | 2025-10-27 05:01:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c411e932-5994-300c-b4e9-48760273bb1d | -12.30621 | -47.44624 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e8d6204-493c-3dfc-8957-4b3dd3baf033 | -10.82684 | -47.6261 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25f4f5ac-8ae0-363d-b7ee-7ef4d144620f | -7.83494 | -46.46129 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 149c8309-7128-3d21-984a-c05bbc397529 | -10.83166 | -47.6268 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b400f340-9017-3744-b69a-e28f961ac43c | -11.03371 | -54.26699 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2be03a5a-e11c-391b-8a6f-a5039e4abcee | -11.42409 | -46.11151 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12a4e1e6-b742-3070-a24b-a24f07802311 | -8.31635 | -46.18007 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb126b56-8db5-3fb5-9f98-1b71d93d386e | -9.13288 | -45.85975 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0838eafa-f58a-31e1-99ee-0b11406d7aa4 | -7.9711 | -45.47184 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ebaa9fc-6a25-33fb-b135-c14bcae8f8f5 | -8.05815 | -54.9266 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce11bf8b-3fa7-3df3-8b6b-5fdb54e1715b | -8.06798 | -46.94619 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5fa8c23-7c77-30b6-8899-390221237dc2 | -8.88585 | -48.00034 | 2025-10-27 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 529bd166-9063-3c43-bad6-56bf4733de76 | -6.63722 | -44.62584 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09e27aa9-0967-3831-a034-d43760fad4bb | -9.26989 | -45.59778 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592edb00-9609-3e82-a403-fc02e38dcd95 | -10.64008 | -52.18514 | 2025-10-27 05:01:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a5cfe84-46e3-33e3-8bdc-25c3feb94755 | -9.72416 | -45.41807 | 2025-10-27 05:01:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f7c6bfb-18ea-32c9-8ad0-7b656e6eb6c9 | -8.31003 | -46.18799 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93ef4ab0-7e67-3b33-bd39-6fc59dfcab8b | -7.87989 | -47.24782 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README62.md)
