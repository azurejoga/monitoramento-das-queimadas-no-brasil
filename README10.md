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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed97419-251a-3d66-8c44-989ecbec8452 | -3.32153 | -42.30119 | 2026-09-11 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 951a98f0-e6af-3c46-bf87-c224ef73dc1d | -0.92997 | -47.1921 | 2026-09-11 04:06:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e00732ca-e20c-304e-ab32-6551ba5f7f9d | -3.06508 | -49.52128 | 2026-09-11 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9669ed88-abb2-36a7-9910-424a734edca4 | -0.92895 | -47.19129 | 2026-09-11 04:06:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5872ae3-04ed-34a6-92c9-7c745585c01c | -2.70329 | -42.72878 | 2026-09-11 04:06:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1e7690b7-3976-3371-a5cc-15acb24dd924 | -2.93502 | -50.47452 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9b915a-b30e-340f-b768-598d4cff5cd0 | -0.92492 | -47.1913 | 2026-09-11 04:06:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fccc5df0-510e-3bc3-9660-d80b7339e42d | -5.03191 | -42.47411 | 2026-09-11 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12fa8a53-2961-3108-a66d-4d4f2ffc68f1 | -3.53174 | -48.1864 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f408dd75-c3f0-3269-82ff-269340e16ea7 | -2.89215 | -48.2788 | 2026-09-11 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c27dfb2d-531c-3c61-8fe3-737dab95c7c4 | -2.88171 | -40.02293 | 2026-09-11 04:06:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a43117c2-96d6-3039-81c5-e01de029b0ab | -3.36472 | -50.76094 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb80855e-5782-3f6b-a17b-483b4420f756 | -3.07059 | -51.33838 | 2026-09-11 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8900f9e-9fe0-317d-95ff-3165433ab6be | -4.07455 | -48.25628 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e8c6e25-e55e-3871-a43d-cdf5f2cb94b8 | -1.45915 | -49.35978 | 2026-09-11 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 505d8496-8d6e-3e48-8e0e-5645f50b1d05 | -4.27973 | -46.53558 | 2026-09-11 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e883ab24-6e2e-389d-989f-c30e396d9a49 | -4.3647 | -47.778 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0e89ad41-25c4-3893-904f-9c8a46655673 | -3.37698 | -50.76311 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0ec15fa-b778-3944-9518-f0c242c7aeeb | -3.37781 | -50.75832 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c27862c4-2913-3329-b684-e2c8d8cde436 | -3.36553 | -50.75624 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a7c531f-ae8b-3cbd-8d2f-82c256d38658 | -4.35974 | -47.77713 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0dbda9b1-145b-34ea-ac55-fd477097222f | -4.2805 | -46.53082 | 2026-09-11 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e9114d3-4c27-3a9f-b87b-b6433f88f07a | -2.93949 | -50.48518 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89109b7-8725-33a4-a010-e7b8af253415 | -2.25071 | -47.98973 | 2026-09-11 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c397c98-2ba5-3dc2-9b33-cb33d6cbef6b | -3.37087 | -50.76192 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 952193a7-15b5-3e98-b2b3-5da95b315f1a | -3.97118 | -41.52311 | 2026-09-11 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b898976-6fdc-3b8b-8c0a-422839a14cfe | -3.53278 | -48.18018 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07765527-bdfd-39ec-9c24-5daf0f5a5bd6 | -3.53226 | -48.18328 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fee414d-ce77-3d47-9f10-265e929adf10 | -3.07079 | -49.52222 | 2026-09-11 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03b6af04-0cb1-3d25-9012-e6b1c0fcaf29 | -3.3251 | -42.30174 | 2026-09-11 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 75bf6bfc-874f-369f-a84a-e7574bd6fb41 | -3.51857 | -43.26071 | 2026-09-11 04:06:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8866b077-44e4-36e5-b78f-4395a5ddde69 | -3.95403 | -38.35557 | 2026-09-11 04:06:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 37333772-af03-3da2-9e40-53041008defa | -2.85907 | -49.53983 | 2026-09-11 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8936a96e-50e3-3411-8130-35cf232b017c | -3.94465 | -49.40285 | 2026-09-11 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbe535b7-ae3d-3e16-930c-2f88cdc76d18 | -3.24728 | -50.82174 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ac785f7e-5718-39f8-bdc2-15ee98f3121c | -2.94108 | -50.47564 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 510bcec6-75e4-396a-8120-4141d01f733d | -2.94186 | -50.47558 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb5aceec-fd28-3b23-b67b-dff9321f3640 | -4.82761 | -42.88642 | 2026-09-11 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9d84989-c3d8-31d0-a018-2269758ebb38 | -3.54781 | -48.18576 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69598564-ec7f-3949-8c55-4aff6c20e852 | -2.9358 | -50.46987 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e4c4d01-5690-3c22-b191-d79a26d8412a | -2.9456 | -50.486 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d824f87-e82a-351e-858b-3748677377d6 | -3.37168 | -50.75721 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c19b6279-088e-309c-99e7-86c8af0accee | -2.93423 | -50.47926 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fe493d0-2bba-39df-87da-896a8f98c49c | -3.97177 | -41.51939 | 2026-09-11 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d74cce8f-f531-31ac-ac60-a3830e991c82 | -3.69168 | -44.16149 | 2026-09-11 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2851d77-f604-38e2-8d30-c9446a903378 | -3.7586 | -49.36785 | 2026-09-11 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc7308ce-0977-3718-9554-70492373d97b | -4.36378 | -47.78355 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f7cbd84b-629b-395b-b4bb-c7eba93e0196 | -3.55932 | -41.11821 | 2026-09-11 04:06:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 61f84fa7-0d33-32cf-a11d-9ccfc44016c5 | -4.35881 | -47.78268 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6263ce9-fd76-3994-b831-d3f3febbc4b1 | -3.51557 | -43.25563 | 2026-09-11 04:06:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10cb6aa3-70f3-3cb9-b1b2-ccfa30a30f46 | -3.36635 | -50.75153 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b24bd8a-439c-3387-97d2-422fe3ef55f5 | -5.03128 | -42.47803 | 2026-09-11 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6e62e81-955a-365c-a0fe-ec54eeaa4f52 | -4.17055 | -48.70975 | 2026-09-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0773dfed-5b8d-3147-97b1-4b6e8b1a109d | -2.94021 | -50.48509 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18eb142d-441f-3800-99df-7b301418e778 | -2.94029 | -50.48038 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b976779-f8eb-3392-bf3a-0e7396e03366 | -3.54833 | -48.1826 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02a929f1-0cb6-316c-8a3d-af440edcf802 | 1.29038 | -50.68491 | 2026-09-11 04:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5fa1286-b41a-38ad-8de4-7548c8999bba | -2.78408 | -47.61987 | 2026-09-11 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37d6e798-0ba7-3047-8712-315f6b878bc9 | -0.92846 | -47.19427 | 2026-09-11 04:06:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99a831b6-5b70-3b2a-8c5b-d76e0ce3c60f | -4.1711 | -48.70657 | 2026-09-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41004da6-dd68-3bc7-941b-a39aa38e1e0c | -5.4197 | -41.8484 | 2026-09-11 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ff0c4ce-5d51-3aee-bee0-5481879396b2 | -5.00365 | -42.98073 | 2026-09-11 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4a53ab9-fda4-30e4-a2a1-b9c3f8306aa5 | -0.9295 | -47.19509 | 2026-09-11 04:06:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 369f342d-4c1e-3bd1-ba24-6707ea215888 | -2.94105 | -50.48023 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79185aed-66a0-3643-aef6-64037146abfc | -4.35485 | -47.56542 | 2026-09-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b4713fb-737e-38c9-b054-31c85f90d2e5 | -3.54367 | -48.17865 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc88f6ca-b0f9-317c-873b-84dc70a3c07f | -2.25123 | -47.98659 | 2026-09-11 04:06:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8de00f3-a4a2-3691-8027-694972bce392 | -2.94186 | -50.47101 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdd1d018-90f3-34c4-83e7-ded085157a38 | -3.53693 | -48.18721 | 2026-09-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7562c17c-b651-3a2a-a2ed-3e517c6029d1 | 1.28383 | -50.68595 | 2026-09-11 04:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54a33d77-492c-3d75-a110-2827da41d3e0 | -4.82829 | -42.88224 | 2026-09-11 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67cd6e01-63c1-3a9d-b2ec-dab246d574da | -3.06443 | -49.52516 | 2026-09-11 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 433a4882-8bb3-3632-ac4a-f3484cbf4421 | -3.36716 | -50.74682 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46532e2b-cd8a-3985-aa27-88d33f21d8e2 | -3.3725 | -50.75249 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 371051af-661e-3f61-8ffc-2094b5c199c7 | -5.24659 | -40.59681 | 2026-09-11 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 23b3ab5c-ad6f-3582-8eed-6ecc8ad537c2 | -3.5193 | -43.25623 | 2026-09-11 04:06:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fccae579-5a22-3baf-9bef-09ee9acb7d66 | -3.10406 | -39.77832 | 2026-09-11 04:06:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a8aa1cf-99a8-36d7-90c8-8b74145428d7 | -5.4191 | -41.85208 | 2026-09-11 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bf9a9927-3f36-3d28-a910-3b748c8589bf | -2.85842 | -49.54373 | 2026-09-11 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e3b587a7-24ae-310c-a21e-409bee28a9df | 1.28469 | -50.69148 | 2026-09-11 04:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f61fcc3-b412-3e40-8407-d218fda12a52 | -2.89173 | -48.27729 | 2026-09-11 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb58515a-e313-3d4b-932f-4a7e9ca27775 | -4.95268 | -37.4412 | 2026-09-11 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dbfcac8b-99c5-34b2-80b4-9009f87363c0 | -3.32218 | -42.29713 | 2026-09-11 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8b3859c5-455c-32d6-ab7a-b2d1f118a5ad | -4.28028 | -46.5329 | 2026-09-11 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 79f7815a-0a93-37ea-a45b-62c12e030b55 | 1.28952 | -50.67939 | 2026-09-11 04:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c85ad8a4-bed6-3e64-a8de-bcd3a1067574 | -3.30808 | -39.34786 | 2026-09-11 04:06:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21a96364-f2a9-3450-a92d-897e7e2812c7 | -3.37004 | -50.7667 | 2026-09-11 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 438f5f1a-194f-30ab-8495-6acdae7e05e6 | -8.70876 | -49.61787 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5ab8ad14-0ac9-3759-8989-ef8591b27e39 | -10.13536 | -36.31282 | 2026-09-11 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 7dc96234-5ccb-3e98-b1ed-49f2064334ab | -6.28876 | -41.70259 | 2026-09-11 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 925c2d5a-031a-3cd6-acc8-ecba3b113a29 | -12.37976 | -43.43958 | 2026-09-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc3502ce-af75-3b2c-920d-562b43131926 | -10.77648 | -45.94365 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c83216a2-f971-35d8-8c4f-81b936f35caf | -10.77893 | -45.94641 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 711480c2-2b09-3775-bda5-cd4ac9f7998a | -7.9272 | -49.73404 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58039ef4-abfb-3a09-aa4f-896869fc0a07 | -7.18141 | -43.61608 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0557e0d-ca15-3fcd-86e7-b938e18631ed | -6.01854 | -51.33321 | 2026-09-11 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae982d04-c470-3c3d-be91-395a414f5098 | -8.62619 | -47.41131 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8104f479-c84a-3fd6-9e80-e639c6aba87d | -9.60524 | -46.77584 | 2026-09-11 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 357ccc0c-dcd1-3270-8ee5-c025c6116a42 | -10.46963 | -48.65036 | 2026-09-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4b718a3-4db7-3f23-92d4-e0610ca70753 | -7.80825 | -42.77943 | 2026-09-11 04:08:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README11.md)
