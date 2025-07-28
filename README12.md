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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9af72036-5faf-3299-9dce-fce511f2af60 | -7.80643 | -46.57035 | 2025-07-28 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5805125e-1ac6-3b6c-8ef5-e3392fac6772 | -6.91853 | -44.25163 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0486fef9-1090-3828-a39e-23f4898f1fcb | -7.1137 | -44.92377 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09bd1d2b-7e4f-3e93-b058-fc0c0f27fe93 | -7.69442 | -46.04496 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e53ac93-72d4-3c87-8e6a-3170335a96ec | -7.35374 | -44.72225 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b84c2a6-199d-36b3-b8ab-844080efafeb | -6.39511 | -43.37974 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 715d6c88-c082-3ccd-9969-f1397ab60f06 | -8.29101 | -45.00815 | 2025-07-28 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 531089e2-2f47-3aa4-92fd-7e18d810c5be | -6.17491 | -58.06939 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ad59f27-265b-3998-b515-f7daecdc426d | -6.3861 | -43.6875 | 2025-07-28 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54c6079b-b33e-3d62-b3c1-bc75465277c9 | -6.39874 | -53.36192 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bdf60e7-642d-38ab-947c-8b8f01a83c81 | -13.11208 | -47.37275 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edd32f5e-7f07-3b8c-9691-0771555cd4bc | -7.10418 | -44.93354 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cbbbeda-5850-3a51-8d09-6c060c12b57e | -6.49082 | -56.20749 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f793e60-921e-38dd-98d3-c3e89502c00c | -8.74284 | -46.6873 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84ad6497-c7ce-3ebd-8941-0c7a70fe4df5 | -6.42665 | -41.14831 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3b378da-d2e1-399b-b284-66d67c3cd9bc | -9.46132 | -57.84942 | 2025-07-28 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22eece49-ccef-3d4d-b131-3441f3f02ef3 | -12.74696 | -44.73676 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d386180c-7731-3fd9-a3ea-9772792a72ca | -13.12392 | -47.36965 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 913e9371-fcce-3e31-9a2a-01ef3891360f | -13.11271 | -47.36832 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bd1bce3-837c-3935-9e07-63ba2958a26b | -7.80511 | -50.77886 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a8468e-2187-31be-a209-0c2e1542b156 | -13.13144 | -47.3702 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2abc3865-b721-34b3-bd2f-f9f50078bc96 | -6.54753 | -56.18923 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408fc829-b4fc-307e-8745-35e8159a44fc | -7.82598 | -44.58993 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c97041b-413d-3da3-843c-4b32b386d0b3 | -6.44997 | -53.36376 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6027392-687d-3cdb-9a1d-9a49f5e276b3 | -11.87643 | -55.44955 | 2025-07-28 04:40:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d27e5bce-09fa-3156-84c9-1ae36478e2bd | -6.25389 | -44.96907 | 2025-07-28 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0878253a-df30-340a-b8d7-71a8ad17e6ad | -6.40093 | -53.34855 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 445766d8-b0de-3b24-8a9e-e44d09b8607f | -7.35073 | -44.71465 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eec434ca-cb73-32c8-a585-1768ebe41755 | -6.82083 | -44.14916 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81696217-6700-3f1f-91a8-5ad13bf3d4af | -13.09312 | -47.31876 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78b14562-3aac-3e5b-a1ec-1265198c1d3c | -7.35427 | -44.71869 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bab18cc-7291-38a0-8c7f-7f2664da5107 | -9.5981 | -43.86479 | 2025-07-28 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9d168b1-9b97-388b-a70e-86b12acab0a7 | -6.1744 | -58.07237 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ead2ffe-0af8-341a-b9ea-578c354996d7 | -10.62894 | -45.22555 | 2025-07-28 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0477df44-0b76-3170-bc7b-79ced74dd6e6 | -6.49751 | -56.19489 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6a7e6cf6-9d08-3a4a-ad93-73727de8f5c1 | -7.35427 | -44.72268 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e198aeab-566c-352b-8945-742f7a3b34bb | -13.1199 | -47.31786 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06567269-4e74-3a03-a77a-a37646a17bcd | -10.45478 | -46.51361 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a6fd526-ac9b-3a6f-a41d-7d7fdc39f7ce | -7.65868 | -44.79934 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1a4543f-80f9-3ed9-b2bf-4c3c409d30f3 | -9.63662 | -49.4827 | 2025-07-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7970b2a6-9e7c-3f8f-94f7-8f7fc62922ef | -7.295 | -43.08257 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd0e6873-673f-3d9e-a4e9-1717b5691585 | -6.54309 | -56.18845 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3370177-d688-36dc-9f85-a18cfa5a4981 | -7.5417 | -44.42806 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 136ee9e6-fd66-3978-a4c1-6829ee61e032 | -7.8053 | -44.59523 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e78cb2e3-82a6-3b78-9ba3-7af3d0e28f98 | -7.35121 | -44.71504 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c057d1f8-0a31-3f3e-80de-27aa529823db | -9.29417 | -48.32462 | 2025-07-28 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a229613-c002-3f0e-bd9c-40ee559a9a38 | -10.31358 | -54.15386 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80a50b55-0c8e-3b6f-bf6f-8172bd6a06a4 | -10.04008 | -59.1049 | 2025-07-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86f34008-4964-3992-862c-dfa2af4b7edf | -8.45332 | -47.51619 | 2025-07-28 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e53902-bf1a-3e01-b137-0da9e19d234f | -8.10803 | -43.05945 | 2025-07-28 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4a51f0b3-eeac-370c-9af1-2ed3af15584f | -6.45224 | -53.36142 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c012c169-4710-344a-a34e-5f5964d6fbca | -12.74741 | -44.73908 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdce47e4-26ee-31fe-a0a4-c0895acf676e | -9.04877 | -40.2525 | 2025-07-28 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 399e20fa-89da-30d8-91c1-ca4090e8898f | -7.09642 | -44.9418 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3c96a23-63d6-3707-9570-777e11128b43 | -6.44696 | -53.34683 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b94b5f1-381d-3446-b7cf-1dcfecbac53d | -7.53757 | -44.42738 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7caf45e-ceea-36e8-88ef-38ee72b37983 | -7.28724 | -43.07204 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c77b4cc3-70db-3e3a-b574-ea7248bfd4ee | -7.09324 | -44.95358 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fb9303f2-1dc2-3a03-84fe-a6d04f002a08 | -7.21584 | -44.16895 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3933ed2b-0407-3197-8c7f-aee2d0f47842 | -7.24312 | -45.38562 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce9d975b-77bc-398b-8dba-e8ce913537aa | -9.02371 | -59.75758 | 2025-07-28 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a1d4b61-3148-3ec6-b47c-c078ff2e1b28 | -7.15204 | -44.36597 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eb29afe-cd13-31ef-a81e-2d0176a5c1f5 | -7.09091 | -44.04161 | 2025-07-28 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037d03b8-9071-37cd-a0e9-71850c8d04e2 | -6.17572 | -44.41329 | 2025-07-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73185f98-8e3a-3582-9701-cee2fbc95c39 | -6.39648 | -53.35241 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 703ebbfa-a522-3e5a-ab81-25dcb4d61d28 | -6.49676 | -56.19932 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b7452a5-ff13-3aa0-b513-74ec2aec5c73 | -8.45391 | -47.51226 | 2025-07-28 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66dc0522-de48-3a7f-8360-ef5aee70cca5 | -7.35684 | -44.73372 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f193b15-db58-362d-bd43-41000a6daf33 | -6.42196 | -41.14471 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 44a8e9af-a6b6-39f4-be82-96cfd67e7b23 | -6.63706 | -43.03303 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27201884-359f-39eb-96b4-9cd2d994fe04 | -7.35241 | -44.35869 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22aa42b1-f234-3f86-9452-08b75bcc96a9 | -7.35181 | -44.74008 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 879fa5b9-aeca-3364-a251-365e202bb69a | -12.71816 | -47.01686 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b25fe72-3ad6-35c4-9a9a-bd62ccd36a3e | -7.2424 | -45.39048 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38e0a0d5-a1e0-3a83-8976-85da5f6e1d44 | -7.35477 | -44.7191 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9559c014-816e-33fc-a1d0-1991ea72bd4b | -7.42165 | -44.71426 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 926b071b-7b75-33c2-a845-e5816d39b66a | -6.4071 | -41.13938 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 067ffbb7-1544-31e4-8eda-354eff3f9274 | -7.6991 | -46.04769 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bdf291e-e603-3b05-b97a-f45aea61b725 | -11.52329 | -54.68463 | 2025-07-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb5bf3f9-242a-304f-9e84-2695580825b9 | -13.13019 | -47.3524 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d94ede6a-846b-3029-982a-56f14507373c | -12.06119 | -48.77357 | 2025-07-28 04:40:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bcae81-2252-399e-889f-b6c50e7fcc56 | -6.92485 | -44.23713 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 660f5ec8-ac39-355a-a1a1-4ab818b031d3 | -7.10287 | -44.95307 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 899428a5-e04b-33ee-bd78-5983bcc25322 | -6.82834 | -44.76499 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b307cf4-196d-3b7d-9e5c-57d63d47702f | -7.35126 | -44.71111 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12201d19-38f6-3265-b34e-f6bcccd80fd5 | -9.64095 | -48.28038 | 2025-07-28 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b94775-7707-3e4f-a1d2-8f18a5c3fe9e | -6.55122 | -56.19434 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e6936b3-2f44-3090-9d9c-1e2dbaf0369a | -12.6671 | -47.02378 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3438fa4f-2579-340a-a147-85747cd496c9 | -7.6947 | -46.05167 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a07106b-3c07-3d2b-b8bf-81ffc0018e6b | -7.69681 | -46.05458 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4abbce42-f39a-331e-883c-cf13bfaad1ff | -7.11247 | -44.88861 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16dcfddd-579f-3caf-ba45-8e94f32098e1 | -7.04059 | -44.33026 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2f87685-3738-33a2-be1e-e0fc551f82a3 | -7.38331 | -43.44707 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f65d77-e992-39b7-98ea-0913226ef6c6 | -6.1805 | -58.06731 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d13bf22-8e81-39a2-b971-c5476b09cd64 | -8.73918 | -46.68675 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65891618-8784-375b-86fb-7ca8cb115d4d | -7.11511 | -44.91392 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a495d1e7-0e0d-3626-8c56-df182feb92cc | -9.44612 | -43.19881 | 2025-07-28 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7cb5f9a-2902-3c17-a255-ca7d8819d4aa | -7.41813 | -44.70998 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4191e6d2-0b15-330a-9e76-d20bafe60349 | -7.09723 | -44.954 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6ac1da0e-f514-39c1-a670-692794aef4ba | -13.09745 | -47.31503 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
