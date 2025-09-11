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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9220e7d-7869-3914-ac13-8ca8322920ff | -10.56861 | -52.04311 | 2025-09-11 03:55:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 355e1654-16e7-34d6-b70c-522771e79928 | -12.67725 | -40.61178 | 2025-09-11 03:55:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 381c0e68-9390-3a9f-b043-c62cc272cf9f | -8.03721 | -48.68244 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1ead286-c00b-3b7f-bc16-e4d4b000b5be | -11.47783 | -49.26295 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f98790db-3a4b-3e85-a714-9974dce4fc07 | -11.15849 | -45.30791 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bef7309-f478-320a-8ff3-e180b0a3a7e9 | -7.2667 | -39.38366 | 2025-09-11 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 771ef54f-eccf-33bc-868b-90ff0c87783c | -7.55972 | -48.20618 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0de8cea-475f-323f-91f4-f080838229cf | -7.53874 | -44.6778 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 092b8339-02ce-3102-b10f-ec917d00617c | -11.47652 | -43.64272 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 950d3bff-7e10-369d-9f3a-4546e5b3d97b | -11.16197 | -45.31257 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6618801-6e28-30f6-897e-32e03cf35302 | -11.46251 | -43.61168 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 726e2f3e-c951-3dba-b276-9e10fb463884 | -9.67607 | -47.51965 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5208583a-dcd3-33bf-887e-d6b390cb29ab | -6.20588 | -43.49314 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e183e91-aa4d-3381-b3ad-cd0a6791cefd | -6.39635 | -44.03308 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8022ed87-33c6-3fae-b859-422797315728 | -7.56986 | -44.01547 | 2025-09-11 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18fbd2f3-0e5f-3329-9f44-687451f0dc03 | -11.37412 | -43.5132 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59f32185-94fc-3b6d-9593-ed8f5b715323 | -11.47198 | -43.64672 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38e8a27e-f845-3d7a-a1e4-b2e1075ed117 | -13.26561 | -43.74871 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0556f1f2-6f4e-32ba-9105-7720a22918bb | -11.71597 | -50.6438 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ebc0b645-2ec5-3ab9-a084-403e13f49e17 | -12.58614 | -44.79037 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 576a38ca-f67a-3a7f-9c35-f88929678012 | -11.15364 | -45.28671 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 496224de-905f-3f97-b4a2-f1303af43c5f | -11.35372 | -46.50262 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3bdf0ffb-82c1-3597-a804-5931e3549838 | -12.1038 | -51.02527 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c8d9546-a6c4-3bdd-bbd1-00e7dd029646 | -6.48458 | -41.75011 | 2025-09-11 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3648b2b-026e-3241-a2fc-621e112aa158 | -12.12532 | -44.86303 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e37cdd88-4b34-3e3e-9b5e-b8e83be97d8b | -11.40608 | -43.55151 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4283d9c9-340d-3aa4-b448-bbae0cc4a71c | -5.59919 | -48.11801 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8776b4bc-f4b4-3e85-9e00-1d0e978136f4 | -5.76796 | -45.52396 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6eaa89ff-d432-3ad1-bdd1-8604d5e07b03 | -7.22118 | -45.31253 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d35ca1d-ef44-3fe4-893a-6bc4e648b9d6 | -8.75309 | -47.10504 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06cb09e9-2b15-3592-92af-a0924aac3eba | -8.73435 | -47.09627 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b162a146-593b-3d37-90ac-e815a2412a27 | -9.90574 | -49.91512 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c121ef-3cc7-3388-8f6d-cb1bbfeb68cb | -13.15579 | -40.6841 | 2025-09-11 03:55:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 78f026c5-a8d2-3380-8029-49599e6e47ea | -8.81136 | -48.09612 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52e117e0-5986-33ce-859e-59c0675fbe8a | -7.60944 | -42.53638 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb5e27db-885a-3e7e-9d87-fbaa897f2355 | -11.43219 | -43.57945 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5930e303-f9b2-3f90-a50c-fb17a1f3535e | -10.31943 | -48.81203 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 270e1f17-7be2-3204-9141-e2c665ea6e09 | -13.28909 | -43.76666 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02e597d7-b3b9-3cbe-93ea-30854d5f1d21 | -9.1231 | -46.19394 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ca15a13-894a-311a-b07d-f3079905313d | -11.15614 | -52.03341 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 207bdeeb-9457-3627-a4d9-1529bd1c0252 | -11.42766 | -43.56786 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85765f49-b2a7-37db-abf0-5dc0616b021a | -9.03758 | -45.79212 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba6c40f5-c417-3777-bdd9-7fb77eb30700 | -11.78458 | -50.57262 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99eeae3-67be-3603-beb6-ed5b13886ac3 | -9.33864 | -48.9376 | 2025-09-11 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29095c44-5ee9-3c11-aa53-1428e41dd0e0 | -10.26483 | -48.82096 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ecf345-6b6e-35f0-8d89-1fa3b51ccaf9 | -11.49059 | -43.67382 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f1a1692-3aa6-38a6-9cb9-cca8b0a5056d | -11.96979 | -46.65259 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9120e0e6-b22b-37c0-bf36-3ead48e6cc61 | -5.84413 | -46.1576 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 061c992f-7768-3dff-813c-7c87349dab0e | -6.31944 | -43.41301 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51940db1-8ee5-3172-acf6-0c68a4eee214 | -11.4373 | -43.57889 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 15b2015d-8b1f-39ea-92c1-fd5eece70c0d | -13.298 | -43.75901 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff7c48a-d7ca-3b60-b3f9-633f36445fd4 | -9.15877 | -45.56506 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b180821-3748-37c0-be4a-eb46fcbc32c9 | -11.03892 | -46.05162 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 046c1432-7be0-3cc7-a70e-66d0a014df65 | -11.47967 | -43.62419 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3594ab6-01e3-3d1c-b58b-7ab3dd87e9e5 | -6.40722 | -44.38019 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a34e284-f8db-34c8-919b-cbba9d49e808 | -6.39134 | -43.51108 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc5e9db0-8992-3232-8798-457e34ec8e85 | -12.16348 | -48.48724 | 2025-09-11 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318d55ab-caa3-3972-a173-0b292626230a | -12.10012 | -51.02499 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3532756-7b77-3596-bd4d-9c1f1a9f0e47 | -6.40165 | -43.49857 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c15937e-69a3-30f8-a001-7b5bbf79e456 | -6.25602 | -43.42395 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3ecf28e-f0e6-3ad5-aee4-482f1ec92dc7 | -10.12586 | -46.00863 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e43cce1d-f38e-3413-a792-0a588768c985 | -8.55418 | -45.5545 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60a547a5-0695-32e7-996e-f03ecdf6199d | -7.24682 | -44.42722 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 774e64f6-0b02-3a8a-8638-a18724b78ed2 | -10.51672 | -40.32967 | 2025-09-11 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 746c48a1-b1f9-37e6-a8c8-1bd58ceea1a0 | -8.53033 | -45.69286 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 629b9993-0181-3162-bdd8-52dcc7731996 | -11.41585 | -43.5391 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24cb84c7-5576-3cf7-b31c-48d59be33b84 | -6.67132 | -44.13292 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b33044ed-aaf7-3e89-95fc-93ac8227f3e8 | -9.06227 | -45.70328 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f37a6ec1-71e1-3cb1-bddf-169e8ea4ec3a | -12.10289 | -51.01148 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca8d620-3668-337c-afff-037956034cf4 | -6.44784 | -44.0574 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f089e01-5247-36d8-9c76-7b60e43c8b3f | -12.13328 | -44.86467 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0e7e9d8-e827-328b-8809-42ab711c556f | -6.37082 | -44.48976 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f113cfb3-2e05-3cc0-97e5-a490b2901884 | -9.67348 | -47.53379 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8dec27e-f615-3a22-a41c-06a73e6f1b70 | -7.39368 | -47.37935 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dafb90a-94d1-31ab-bf9f-b046c74da5e1 | -6.39251 | -43.50399 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85a7f750-f304-3a94-8682-8caac66f1156 | -7.88825 | -46.04713 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ea3c074-df5e-39f1-af26-d1cdf1e565d7 | -8.73382 | -47.10934 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2882b96-0fa5-3f1c-8fd5-6c2a8a8b4858 | -10.26542 | -48.81773 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48355e83-5522-33d3-9df8-e39a09187ccd | -11.10323 | -48.41393 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9c57dbb-a8f2-3e9c-bcdb-11931eb197e5 | -7.54006 | -44.67018 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f38f83f-7fab-3d3b-b890-648c1e5dcfc0 | -7.2632 | -44.61277 | 2025-09-11 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b02c439-8535-3cd9-8114-9e7e19acc9e1 | -5.86426 | -44.22714 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 431c6321-1328-3cc9-af4b-0cd4844420a2 | -13.25415 | -43.7928 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a974310-c6c6-3af5-a593-a2ca2ad74fad | -6.57085 | -42.93829 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cd7e750-60b2-36f3-a41b-b393041656cb | -7.98932 | -45.79566 | 2025-09-11 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6bc31b4-1822-3ed3-9029-c81fa6190876 | -11.71426 | -46.50298 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7786472-45f8-3d2f-bcb1-c4b23020172c | -8.16887 | -46.06599 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff76cbb4-9b82-355f-8019-513b11eeb01b | -7.53634 | -44.67059 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9fe825c-dd60-3258-99ba-b7256607e04b | -9.07852 | -47.07311 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b23aa610-834c-316a-b664-da5ffc8814a5 | -11.47852 | -43.67653 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32e14c9c-f057-3bc0-8667-3075c183dbb1 | -7.9263 | -44.8829 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73483770-5390-3c81-868a-3c60fefce427 | -11.99834 | -47.59026 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a60cd3b-cb1e-3d50-9d1c-5558c7e11c13 | -9.1322 | -46.1937 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e83e530-7f5b-3307-b7eb-4e47df9c4dbc | -7.85905 | -48.15926 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c99a4b-2e17-3f6d-81da-03bf343af3b7 | -6.67204 | -38.68886 | 2025-09-11 03:55:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a91b0961-0073-3e59-b773-88880c1e728e | -9.89224 | -50.16815 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e86abb47-fbfc-358d-8e43-a6bb62a1917a | -6.83571 | -45.61544 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 067c0000-ca22-36bc-97d5-f68b045913ac | -9.06987 | -47.06508 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42ce7254-2fa8-3972-866c-ddc5b79b968a | -7.0784 | -43.88013 | 2025-09-11 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b97a9a98-17dd-3117-b5c0-23fd3b84c8f8 | -12.42592 | -47.81179 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README23.md)
