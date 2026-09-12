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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1bdfb7e-b9a9-3afb-b28f-0bb2fd776842 | -3.86275 | -49.22097 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e02a19b-eed8-302e-bfc3-42dac438f3a7 | -3.89684 | -55.8191 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cdfbe76b-f6ae-3ce4-8624-2df37df2e401 | -3.46574 | -51.62643 | 2026-09-12 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff35a5c4-8503-31ed-8ce9-ec4601fde166 | -2.94665 | -50.40666 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 55e8abb0-172c-3a18-9e1b-b614c2433d6b | -3.87698 | -51.18256 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 715e6965-712e-35b1-8bc7-ceb31fbc58da | -1.86863 | -47.98132 | 2026-09-12 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bcd1854-5f92-3aa8-8018-706c2a35e87f | -2.73121 | -57.64529 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 529078af-058c-3486-ade8-b2b2893b0466 | -3.37248 | -50.745 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2992acc4-092e-33b3-865f-3598717b04ef | -5.61499 | -44.84997 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 78376fd3-61a1-3df1-87c5-ae9c54bdcea3 | -4.36373 | -54.77938 | 2026-09-12 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24d6b9a5-1f9f-3ef7-936d-031145188f5f | -4.30009 | -49.11397 | 2026-09-12 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bca7d5b2-894d-34d4-92b6-95267552a147 | -2.95063 | -50.38179 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acea9b73-6ecd-34be-9d53-3e5c85b9f95c | -3.07292 | -51.33791 | 2026-09-12 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b15da54-0f42-3d25-8c95-624f19a712e3 | -2.96175 | -50.40472 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| c616d46b-1889-363c-b425-0f6275cefbc1 | -2.95092 | -50.40306 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b51e782e-a81c-39fd-be88-d00a80ec1fa0 | -4.94228 | -45.6683 | 2026-09-12 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0488c980-2269-3305-8063-b5e0b9b219ce | -1.02892 | -53.73637 | 2026-09-12 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f373ec44-7683-30dc-985e-547bb8856541 | -2.67632 | -54.5874 | 2026-09-12 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5514efb7-5e68-34c2-bb6b-8b560797fac8 | 2.5097 | -50.84723 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e262871d-39a1-32cb-9cad-73555048d264 | -3.38873 | -50.76068 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96e1f11d-f569-3c2d-afbf-d213c04c12a7 | -3.94103 | -43.89148 | 2026-09-12 04:32:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa1b1202-6dca-3ba8-9373-dd0187a9dd2a | -3.47741 | -51.18859 | 2026-09-12 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd67dbf-d0f3-3f6b-805a-decfa6109e1f | -5.76241 | -45.09351 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ed734a7b-fa23-3412-bb1d-c6186d74cfb5 | -3.22902 | -46.95765 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab343a94-b406-3d7d-8d84-12aaecc87ede | -2.96337 | -50.41773 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d011100e-8b65-3aae-b3ac-931ffde24309 | -7.27245 | -46.80174 | 2026-09-12 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3796627a-a091-34a2-9e68-99971c59e709 | -11.04108 | -47.97153 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1aa7cedc-fd69-35d9-802f-141542ab43c6 | -10.53146 | -54.38276 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e67c157-79c5-340e-bcd2-1fbf89e313d6 | -7.46807 | -42.12077 | 2026-09-12 04:34:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b99d4898-d5aa-31fb-bb36-2dbce36aef79 | -10.56402 | -51.36236 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51bfed70-eab1-3a92-838c-f1210d799b75 | -10.69045 | -54.16937 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f37f1b07-0918-3489-98be-32e4b69bb12d | -9.93439 | -48.51672 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a1fdbe3-002a-391c-aa2f-b1c9e2cb73e0 | -6.11553 | -55.6451 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed832f00-1cd5-3dc6-baca-bdb5a23a7df2 | -6.61668 | -44.20605 | 2026-09-12 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8681f802-7d86-3a7f-8ddb-b3b15e9fdc0a | -6.51292 | -47.60323 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 161e1512-3f70-3a5a-8b7a-3b9531700f03 | -6.28573 | -56.03167 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8e17e3e-c0c9-36bc-b0db-da5f30e1351e | -9.60152 | -40.35331 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a7f2cb9-0c6b-3acd-b8d6-d10adb0abbae | -7.41995 | -46.15782 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fb62eb47-6dd0-31c5-b82e-b01d136c5a6b | -11.81014 | -46.36516 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a3edfe1-b138-3417-aaf6-7dbd4bfdb563 | -6.60775 | -58.84556 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 482065fe-6386-3cd4-be4e-e5646fd19883 | -10.5086 | -51.30898 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7f65a366-d434-3287-aece-36de5df0282a | -11.40943 | -47.73654 | 2026-09-12 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5303e9b-03bb-3759-9e21-093a38c77a2c | -10.46991 | -51.35969 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1d350cd-3b79-3a4f-980c-0a23ab1145ed | -9.93716 | -48.52073 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edd0024e-49a9-37e7-8b23-8601e8723be2 | -7.41938 | -46.16159 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb9d34a9-daab-3cf4-823c-9d50ba0c284f | -6.76644 | -59.42931 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3765653-c617-3aa5-9bd2-fe84f121f8e5 | -4.36797 | -55.7727 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feb7d45f-02e6-377e-8d18-b5bf352f1dca | -8.50558 | -50.14726 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1493732-0ef8-3e96-8ad0-62d49122594f | -4.86934 | -56.00429 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6611e223-d9db-316c-bd49-841051517446 | -8.58478 | -54.56495 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a85e8202-3475-33bd-896a-79c1a22d2b24 | -11.80019 | -46.38592 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2631520e-c5f8-3ba0-b1b6-0ab8726aef65 | -14.00997 | -42.14749 | 2026-09-12 04:34:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cd6db6dd-a809-3fc8-bf25-a543979c34ba | -10.55091 | -45.22026 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9bd1fa33-4fb3-3f63-9482-d646d61617d9 | -12.383 | -47.38638 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fec55f9-5061-360f-b96d-d345aa627c3a | -7.9614 | -44.00352 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b70713e-7624-3b15-a62f-b55916fb3f92 | -7.60716 | -46.12277 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e45a1772-a54e-3fe8-b674-5f42fd06a680 | -5.8318 | -53.78996 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21d934b6-b711-31e4-90ff-79104cc84735 | -6.11076 | -55.64402 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0b881ee-0cf2-3a48-ab66-7900f680a15f | -12.1212 | -48.9737 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06e5937e-dacf-376b-a7cb-fbe201c5a994 | -7.37868 | -46.03918 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e52e39-4808-3294-88bc-0273f96bd2d4 | -5.1014 | -56.12502 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 584cc85e-91fe-3fed-8fc0-4604af9718cc | -8.94881 | -49.52995 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64ba6df-ec1f-311f-b730-a2957c6e2f53 | -9.93331 | -48.5237 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d35d98-06a2-31e1-a54a-22ce858ba466 | -7.54503 | -47.32429 | 2026-09-12 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e52f5274-9f57-3bd8-88d4-d6faeea96f46 | -4.36846 | -55.7698 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbb30be8-3558-35ca-9e52-2ebd46b0b449 | -7.96664 | -43.99451 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17ee2d90-7c32-3c3a-9f10-cdb3549e80d7 | -5.12157 | -55.9739 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c43cd966-04e0-3538-b2e9-c639bdd54793 | -7.96209 | -43.99871 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41b5bc42-352b-314a-9493-2ae7730f37fa | -4.86526 | -55.99783 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 517921f3-2f83-36e4-a83b-3feb823070ce | -12.41069 | -40.92044 | 2026-09-12 04:34:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4acb13e-5c07-3558-b9ea-75d1daf6a13d | -11.2494 | -54.13431 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 530e876b-d0ea-3477-ad84-b998c1d8b3bc | -12.13883 | -48.96936 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b58d00c2-bdf1-3e3e-be56-5d103eb581e5 | -8.56979 | -54.57503 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afdbba44-1574-321d-a1ef-340869bd7ca5 | -10.48384 | -51.36183 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e00654b7-2d97-340c-937e-ed65010808a1 | -6.43344 | -51.88007 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75db54c3-6070-3f5f-9fe3-91899662e65e | -8.58048 | -54.56429 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91ae22be-dd7b-3641-9e47-159365a6c211 | -6.84065 | -43.05493 | 2026-09-12 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a62b51a6-2016-3d5f-9f87-990742026354 | -11.38771 | -43.97605 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4557f45d-3e3b-3de2-a7b6-7ecb40547f45 | -6.06285 | -53.49488 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6a04529-068a-3dd0-bf47-336408650e7b | -6.52508 | -47.6122 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af4abeeb-4863-3772-b923-abe815e304a6 | -10.55678 | -51.34112 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c10a69e-1245-3e13-ada2-76e545572c73 | -5.1009 | -56.12798 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9ca4bd9-2410-3e16-b1ce-ddd8422fa024 | -10.82954 | -50.58686 | 2026-09-12 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 394272dd-0b2f-3754-9e58-a1634639afa8 | -10.55353 | -45.20238 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6826bfb2-9b3a-3ed3-99d9-77c87da01ae6 | -6.95933 | -44.55107 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a2bbbe84-ddfa-3a8a-86d4-5769ca1f134e | -6.2674 | -53.11676 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cfc6584-f658-3f5f-a610-a1e506fa7ba3 | -5.73994 | -53.47847 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e642d62-23cd-3c3a-bd6a-3224b6ef827b | -10.74926 | -46.20388 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bdb32d4-6c63-33c9-88fd-3f511773ce89 | -7.1152 | -42.10789 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffb52b86-da00-3657-aa48-d5f282790367 | -10.37237 | -45.12642 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12d9d504-5cb0-3c87-8661-fd3f01992a2d | -5.80419 | -57.72925 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967ec8ff-b0ff-378c-927e-669dd998e2b7 | -8.03223 | -43.76141 | 2026-09-12 04:34:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8d993458-8ab7-383e-b72c-dc02e006703c | -6.6701 | -45.90027 | 2026-09-12 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d28bbc8-963e-3e73-b4bf-9bda82c5c914 | -10.72221 | -48.96119 | 2026-09-12 04:34:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ea72ba2-35f8-3ead-aa28-708ab7bf60db | -10.49475 | -51.37103 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d8cf351-680c-3071-aede-ff7e9e6e49d3 | -9.60073 | -40.35921 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b83ba41-697d-34c8-a93f-88bcb31ed3bb | -6.10027 | -55.6475 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2bdc17f-387b-340c-9208-a5c5544d9c41 | -5.79669 | -53.81704 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7fd667d-9ef4-3762-ad5d-ace885d7d3e6 | -7.9632 | -44.01835 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9a823c4-fd7e-30a3-b6db-e1509afa2623 | -8.50169 | -46.37529 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
