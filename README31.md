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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2c25012-50c7-389c-b6d3-895fbe608f94 | -6.53095 | -42.41591 | 2025-09-08 04:00:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83345266-6a41-3cc4-83ea-996dc09d1fc0 | -5.45412 | -42.80456 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d4fa720-50ba-3bb6-bebd-7d3b56f241fb | -5.99182 | -44.14998 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21ccaa04-4f21-3788-bc93-6fd0dc7cad56 | -5.86803 | -44.18349 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34fd68d9-4ae1-3d38-8d4c-0cf7ad6bd237 | -8.2511 | -41.40707 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f40dfd74-8914-3946-ac89-21bd6e08a82c | -6.40183 | -44.46106 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0264283-0c02-31ee-905e-cc54161f6623 | -7.87661 | -46.25286 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3848c79c-5f57-31ad-b005-c8270302553c | -2.14179 | -47.71104 | 2025-09-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b424b7b-9e4b-3714-a0dd-e4a87b5bed52 | -3.45942 | -43.18787 | 2025-09-08 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be13070-41ae-3640-9d6a-ec27eb3d352b | -7.65827 | -44.81174 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22af5d6b-dd7e-31d7-afa3-e7012033764b | -6.99932 | -44.92709 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f343217-d0ed-3de2-a1e6-0f5ca559b4dc | -6.95808 | -43.96635 | 2025-09-08 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b24e999-8a90-3943-b643-438ffc3626bb | -6.62443 | -53.37691 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f6e29556-59a5-3974-bd93-20821fba6259 | -5.44293 | -42.66823 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d3dac411-e800-3988-9b67-cafa6c82356e | -6.39049 | -43.81161 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11c6444a-0dc8-39ae-ad43-bf489f3c66bd | -5.37128 | -42.63591 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 76f474be-b688-3786-9c20-fc0c9ae197bd | -7.76799 | -34.90806 | 2025-09-08 04:00:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 8e10d8ba-adc9-3f6b-9ede-0465718f3583 | -5.80949 | -45.65373 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f194439e-fb6d-3823-820a-42d7b2a16f2b | -8.13971 | -44.86619 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e537063-c604-33cb-8d65-1a2073683d96 | -5.43282 | -42.8223 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0a0b2c97-178e-3d0e-a85f-73b0c6f4658f | -4.89625 | -42.21634 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d2f0fca0-4a1c-3bab-bd74-5a10362eb884 | -6.53859 | -44.79293 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffba4f0f-e684-34a3-94a3-b0d63db741fc | -5.8713 | -46.09328 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960b6d8e-b1ce-3d67-a257-2c8865216644 | -2.82582 | -41.73711 | 2025-09-08 04:00:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d7b1a83-5819-3149-822c-dfa98accd060 | -5.74082 | -43.72774 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8ef5364-38f8-34e5-885f-9ac166eb8e1f | -6.71355 | -44.29844 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91837544-7b51-3f5a-b2c9-c9a5f1e6e07d | -5.9436 | -42.95469 | 2025-09-08 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4aee3715-5e26-3f93-add7-f1698e021a22 | -7.57303 | -45.19239 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18cbdf85-2df4-300c-bcc9-eae04f7f5d47 | -6.24773 | -42.43969 | 2025-09-08 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee38595e-7607-37f8-a0ce-76004c9fcbc3 | -7.57275 | -44.00563 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f209980c-367c-3070-87d2-cc206e72c153 | -6.06755 | -43.11745 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f5f6e58b-81f7-36eb-8624-371050184164 | -5.78373 | -45.62529 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09843b2-a25c-36b7-a99b-1dcc5a1fdc40 | -5.44782 | -42.66061 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b46c376-1587-3b20-81ca-3a27bafd06b8 | -6.09154 | -43.71791 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95df3040-9d03-37f3-986a-e7a655d76b30 | -8.24776 | -41.40652 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 584f8a2c-9c58-3c82-a980-5085383d40b6 | -8.62279 | -40.19833 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1594f49f-db8f-3cc6-ba42-198075e41032 | -2.82605 | -41.87069 | 2025-09-08 04:00:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 473eb181-257c-35f3-97d5-558ea215a021 | -6.61991 | -53.36277 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59baf38c-7d59-33b3-b1a7-388fd9dde288 | -4.56504 | -40.34006 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 901ebdbf-8977-3c18-b4ae-9b5d747637b2 | -7.87593 | -46.25686 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f39740ba-4eca-3683-9fb8-927b9b4c0957 | -5.63908 | -42.61849 | 2025-09-08 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34578359-c6f1-34ed-90b1-58ede8b047b6 | -4.57113 | -40.34464 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f55e859e-4af4-3cab-907c-af61adb35c33 | -7.43404 | -45.21889 | 2025-09-08 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b421420f-48ea-38f0-bfc4-b2b004082ca1 | -6.62062 | -53.35821 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7cb9e96-7a06-338a-b1ff-80571dd2442d | -5.82341 | -43.97604 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0946b13-ea72-3a1f-bba7-52aa3117df61 | -6.46418 | -43.95072 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92c8d876-ebd9-3635-965a-b9cb668cbec8 | -6.21531 | -43.28829 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e986383a-58eb-3142-8b95-61b2a680989f | -4.89907 | -42.22431 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c079296c-e204-3ff6-bde2-a3113136ec63 | -5.43055 | -42.81352 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87411ad1-ae1e-38f7-acf5-21750e2e23ab | -5.51477 | -42.66994 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 785bdfb9-599f-3b75-b9f7-600761153a52 | -6.09126 | -43.29137 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e8cb5feb-e0e7-3228-acb9-d48aed7e837f | -6.29825 | -43.33136 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70e91c89-8dfc-357a-b1c1-2d7bc1f239a6 | -6.53428 | -42.92547 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10ee6923-09c3-3fdf-9438-a3ec30fafbe1 | -6.56307 | -42.9511 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 117bca57-9e2a-3f15-b182-ad447f6f329f | -6.25447 | -43.71519 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 700f2fcc-ce1e-3683-b397-386bd56cbc94 | -7.56799 | -43.67699 | 2025-09-08 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| deedf89d-4812-386e-a6c0-8fc6f97eae7d | -5.28799 | -43.43676 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 526dfd88-be8c-353d-b68a-172eab7a8396 | -6.47566 | -43.57468 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d664183e-c126-350b-90e1-c4b22d053d96 | -6.36279 | -42.57877 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79f59642-cd03-3ee3-8e4d-a8235bb97cb1 | -6.25187 | -42.43633 | 2025-09-08 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14eefa3f-9b05-39e0-8195-2318cd226b28 | -5.93866 | -42.9624 | 2025-09-08 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 516f7f85-02ac-3db5-9c42-2fa4407f8bac | -6.46797 | -43.95126 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3456768-9954-3256-ac04-c7e9243cae6a | -5.4492 | -43.44255 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 149dde0b-59e8-3504-b8b7-1e0157b5d51c | -7.42655 | -49.26609 | 2025-09-08 04:00:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aedc19ba-6442-30ce-939b-449a944fe200 | -6.05942 | -43.34791 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d19f6d2a-3d5b-3f46-a1cb-5a65a75362c0 | -5.79538 | -45.65974 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10a71d7f-0e41-301c-958a-4b4455edab37 | -6.20604 | -40.99982 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dfb8f53-a03f-3d57-a66f-e16596dea33d | -6.46528 | -43.94394 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82a19e9f-2df6-34c0-bfe3-a2927ce0ddaf | -4.89499 | -42.22423 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0b18d5ce-a9c8-3d1d-beaf-c1db9c655814 | -6.52713 | -42.92433 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8115c32-8fbf-3abe-ad86-e31fe32b01d5 | -6.64958 | -44.80362 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32899bcf-7bb5-3fc1-88eb-28f34604c3a1 | -8.04079 | -44.03526 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e30d96fe-5001-3c98-bb03-8bab2bc24001 | -5.34896 | -42.64598 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32c00d25-b5f6-3e31-9c94-264fbcbb7e07 | -4.89562 | -42.22028 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 20e68cf1-149f-34f5-88e8-df5ff414066b | -7.16888 | -39.76902 | 2025-09-08 04:00:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a475682-2d48-3d38-9be3-ea204077e800 | -6.19623 | -42.64651 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 94542098-dbe5-384c-80f1-403f176ab91c | -6.25447 | -43.69172 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5ebcc8f-fc71-3b7c-9aa2-5464cf8d6689 | -6.21774 | -45.57333 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e99a55a-d918-3dd1-b92f-afc400e3b394 | -7.08046 | -43.51983 | 2025-09-08 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca729ed0-d6e6-37a1-9161-6aef563aa256 | -6.07032 | -43.32743 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a1c53bf-6e08-3314-8e27-1d7ee5d6c4f9 | -6.43371 | -43.64436 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7244503-2f3d-3e40-bda7-0976e260c9a8 | -6.83925 | -44.87918 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 649ebcef-a488-3a92-9036-25d115a57a0a | -7.22621 | -46.19962 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45fccb58-232b-3803-bfe8-951bac48d59f | -5.24767 | -42.71436 | 2025-09-08 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64676ebd-ef11-35c0-9696-7f38e2390203 | -6.45997 | -43.95238 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce488f56-44c5-3db3-804d-3207905fb52f | -6.15063 | -43.18148 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7735b9ef-c732-3a13-b546-0dbb8af8b92a | -6.2649 | -43.69823 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 357c38e5-13f0-3c63-8be8-61bc84f3f52e | -5.66916 | -45.45758 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3484d39e-53fd-35bb-af21-364a2eca7b8d | -6.92813 | -45.81055 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6ef195a-cdbe-31b1-98f8-41b0765697d6 | -8.4827 | -45.17017 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67334a4c-2f93-3a20-8139-9a68a0cc9c5d | -7.24869 | -44.83189 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0af40a9-3dc7-318a-bc97-ba39044aea47 | -5.06746 | -48.41776 | 2025-09-08 04:00:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6645a31f-2070-3f1d-9862-aeea9e885041 | -7.70915 | -44.72352 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 308eafb0-2b3f-3a91-b87f-b28f4f46d6ce | -6.0893 | -43.12096 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 49cb82c0-217a-3541-9ffb-2fa4a819394a | -6.53142 | -49.50738 | 2025-09-08 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a28cbed5-5a96-3daa-801a-4784441becaf | -7.08207 | -43.89708 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6245c905-aa6d-322c-9b52-efe9e78e9a3e | -6.28012 | -53.43314 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0d44997-c4e0-3f57-987d-cb780b59ee54 | -4.48247 | -48.11942 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80b4b018-0875-305a-b41c-130cd0f18cdc | -7.08281 | -43.8926 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9855b5bf-e365-374b-833c-4913a28ce14a | -6.24817 | -44.82636 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README32.md)
