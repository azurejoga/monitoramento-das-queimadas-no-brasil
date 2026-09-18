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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| accf733d-e56e-323a-be4d-54ee6fd4e52b | -13.2485 | -46.9226 | 2026-09-18 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0be64aca-5905-3b35-aeee-eac2b0930142 | -11.8115 | -46.8158 | 2026-09-18 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 225.9 |
| fd7100ce-e799-31d4-84ec-60d552d07efb | -8.3769 | -47.236 | 2026-09-18 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| fad5d26a-95ef-3911-85d3-ac3db7ff67de | -7.7844 | -44.8669 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6b75e015-8676-3f67-b9aa-14a8f1c3f81d | -2.4815 | -49.3996 | 2026-09-18 14:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 8038de26-7a62-3a34-ba54-139751d05b64 | -11.0048 | -49.7325 | 2026-09-18 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 03172424-f1aa-303f-b1ff-0888a61a402d | -12.0086 | -49.9606 | 2026-09-18 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 2e3016d5-aaef-3bac-9a03-0367b34903f3 | -7.7839 | -44.9127 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| aef25d28-2a42-3264-8efa-0ed65bb024c4 | -8.6817 | -45.4359 | 2026-09-18 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 45098b06-0d68-35d7-bdf4-d24633c0a7cd | -9.8313 | -48.4073 | 2026-09-18 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 508a26af-d978-377a-8b7d-1370f400cf80 | -11.0636 | -48.3118 | 2026-09-18 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 3f65178d-154c-3c9b-b211-c3f05672b2e9 | -9.9509 | -46.6026 | 2026-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 354.2 |
| e658e643-7c64-3798-866a-cce90daaad9d | -11.2979 | -43.3614 | 2026-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| ae7196fe-8e73-35a3-9e58-3a34cc19e40a | -6.3287 | -55.2677 | 2026-09-18 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 8bb7264e-1e78-3a9d-98b5-9bf302040297 | -9.238 | -46.1894 | 2026-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8f71e140-5d33-382a-a42e-fd9e2fe39165 | -11.064 | -48.2898 | 2026-09-18 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a3691b87-bc66-3e34-8dba-5ec2038dd6d0 | -10.6726 | -50.4758 | 2026-09-18 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| d6bbff4b-9557-3e98-969a-da4d5054e599 | -9.9323 | -46.5824 | 2026-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9094ff39-28fd-3df6-b2ac-52ff4dae2967 | -12.5345 | -47.0738 | 2026-09-18 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 7281af44-9b19-3852-b550-d97b8cd34fd4 | -11.8556 | -50.0006 | 2026-09-18 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| f04bf1b2-3489-367c-9b61-260a506a5d34 | -11.2787 | -43.3643 | 2026-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 38c0ac3a-4d0d-36c7-afb9-8b5f72f9ed8d | -7.8033 | -44.8651 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2dad8ad2-3e52-337a-8ce9-a43e19d8ce17 | -10.2821 | -50.0035 | 2026-09-18 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3c636b4c-0cf3-3b76-8a15-440e9ba885fe | -2.0769 | -56.4085 | 2026-09-18 14:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 94aa207c-137e-3083-b9ef-36e0d81c4833 | -6.1653 | -47.5052 | 2026-09-18 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4f1be720-4ee9-3ae0-9679-bb4bc6e4c5e4 | -11.8119 | -46.7932 | 2026-09-18 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 696c8ce9-431d-34a4-99fb-baf402144c71 | -8.5566 | -44.9021 | 2026-09-18 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 30c48ea5-0480-3fa3-900f-0fcfab5427c3 | -8.4329 | -45.7337 | 2026-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8ef6e6e7-cbc2-34a5-bd8b-0d11c78b51b5 | -11.8746 | -47.6125 | 2026-09-18 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4bb7f7ed-3b27-3511-9cf6-03f2b7377141 | -12.5341 | -47.0964 | 2026-09-18 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 17611013-e2c8-3e03-a8bf-319a2dc20b05 | -11.3433 | -44.0376 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 48d43637-8f6e-3395-8cb5-8d0f0a95ee56 | -11.3809 | -44.0788 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 38326961-9646-396e-af36-6a718a4af8f7 | -10.6758 | -50.2406 | 2026-09-18 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 373c6ac7-b816-3e78-b687-c9e16af42ec6 | -11.875 | -47.5902 | 2026-09-18 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6e6da97c-6706-361c-97a4-22074189e252 | -11.9115 | -50.0801 | 2026-09-18 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ef0d422f-bb9d-3a1e-ae05-dcd1d1c9314f | -3.9127 | -44.6505 | 2026-09-18 14:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5d9a6021-9aae-3ae3-8e93-59e9fcf8dce4 | -9.9956 | -50.2675 | 2026-09-18 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 92008aee-cae1-3239-8e36-5966be5f5540 | -11.8359 | -50.046 | 2026-09-18 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 17a51d29-2b33-3626-922b-a0c1e390fe3c | -11.875 | -47.5902 | 2026-09-18 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a76e3ead-7946-332f-9811-91aa09458a9f | -11.8166 | -48.8331 | 2026-09-18 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4ac57618-e547-322b-a087-4585edff187f | -2.4815 | -49.3996 | 2026-09-18 14:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ed2646d1-61c4-3964-adec-873ef25c1cf7 | -13.249 | -46.8999 | 2026-09-18 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b2f9255b-cbc9-39ce-8527-8631b72c303d | -0.5442 | -49.1324 | 2026-09-18 14:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| f8c6e78b-ae24-343f-aa4a-2920b294a2fe | -8.58 | -44.5552 | 2026-09-18 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8a1b6589-88d5-3939-9364-abbe4d842ed8 | -13.6081 | -48.3017 | 2026-09-18 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ffd45718-5749-3210-95e7-cdeaf1d7617b | -11.3442 | -43.9906 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 284.3 |
| b0b82223-d86a-3a6a-bc13-7ff46244c491 | -8.7006 | -45.4339 | 2026-09-18 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| aeb216f9-f82d-3293-a0d4-99cfef973daf | -7.7839 | -44.9127 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 44061caa-e9a8-36c4-9f03-914e28be9365 | -2.0769 | -56.4085 | 2026-09-18 14:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8e455740-b563-38ef-bcaf-687f4977a116 | -13.6148 | -46.9334 | 2026-09-18 14:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3e031707-5ea9-3f67-aee8-bf568c076905 | -6.3101 | -55.2886 | 2026-09-18 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 58a2dbeb-d360-3393-aabe-8e97c229123a | -5.5829 | -48.1094 | 2026-09-18 14:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b8baa736-dadb-3766-a96c-4efc58b639eb | -9.2417 | -45.9185 | 2026-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| db67de3b-ce18-3dec-8d38-d96193fcad80 | -6.939 | -43.1188 | 2026-09-18 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| dffd9748-9d84-3d93-bc2b-b2faeb12aa50 | -11.2979 | -43.3614 | 2026-09-18 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 644.5 |
| 73dba522-5eb1-3d79-8ee3-1433cfe73e6c | -10.6944 | -50.26 | 2026-09-18 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 04204d6a-8669-31cd-8602-cf3878a77de1 | -8.6643 | -45.3241 | 2026-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c50bd01f-cc32-38d1-92e6-4d0f20681a2c | -7.8601 | -44.8366 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0598a907-0ca8-395b-bd23-c65d582d75d5 | -9.8502 | -48.4053 | 2026-09-18 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 33787115-e960-318e-9848-12a3195d58da | -10.5838 | -48.696 | 2026-09-18 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b92d9e82-e656-3036-bf22-0d83a37cda40 | -10.6758 | -50.2406 | 2026-09-18 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 9a85a2d6-5338-367e-bc30-c6ed5c983ba9 | -11.3446 | -43.9671 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 3f610a30-a1b7-3892-8823-3ed6f06c7976 | -6.0168 | -52.182 | 2026-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4769c826-c9e1-3717-9363-a4b590c2d4b5 | -7.3564 | -44.4726 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f060690d-3711-3cf7-86f2-4ac4da95fc34 | -12.1527 | -46.9933 | 2026-09-18 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b1de3a74-a76e-34e4-aa5a-40c51395243b | -7.8033 | -44.8651 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 29774006-7f0e-35d1-a95a-d4177acbef75 | -12.5341 | -47.0964 | 2026-09-18 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 149c30f8-315e-300c-83e3-a07a129e45fb | -3.7333 | -54.6499 | 2026-09-18 14:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a086e2c5-35e5-3161-84aa-f0dc272ebba1 | -7.841 | -44.8614 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5e5b7604-1f31-390f-90b0-c5eda051fe2c | -11.2971 | -43.4088 | 2026-09-18 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 788ceb96-66d0-390d-9940-7db9a2b63b6c | -6.3287 | -55.2677 | 2026-09-18 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 34fd5b7a-8070-305a-9828-f46b1bc7315a | -11.0643 | -48.2678 | 2026-09-18 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 869dfcc9-528b-3a5f-9c52-0c5354919b28 | -7.1675 | -44.5589 | 2026-09-18 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 766dc4d9-e7d9-38f2-ab95-96c049540fde | -13.2485 | -46.9226 | 2026-09-18 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 7e144e35-a303-3f4a-9798-84aa10808361 | -0.803 | -48.6611 | 2026-09-18 14:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6d06117c-7819-308a-94a3-a8a96cdd3582 | -9.699 | -54.8176 | 2026-09-18 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8b9e4dd5-c3f1-34f9-ac1b-1ac48348d699 | -12.5345 | -47.0738 | 2026-09-18 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d079a3a0-7607-3b8c-a698-1d2857b6bddf | -8.6832 | -45.3221 | 2026-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e50d1939-4d9d-34d3-87df-61e8223c7e4c | -12.9243 | -44.7484 | 2026-09-18 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6bab44d8-6b2c-3f82-80c9-10becc271147 | -10.126 | -46.2899 | 2026-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a6ec7220-5be0-3c3b-8fa8-5b4550c87448 | -15.6117 | -56.5537 | 2026-09-18 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b399be30-6e54-3ed0-aa14-794963759b01 | -7.8027 | -44.9108 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| f8cc6c0d-8e61-35b7-86c8-6584dc4ba505 | -6.4076 | -47.5319 | 2026-09-18 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 577d534b-8678-3459-b70f-6ad2fc282f01 | -13.4303 | -51.9036 | 2026-09-18 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 216.7 |
| ea869645-d463-321d-a435-e1dd6e5e2db8 | -12.0902 | -50.8521 | 2026-09-18 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f28fba5c-5838-3fb5-b02d-e779826595b4 | -14.1732 | -45.1875 | 2026-09-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| a8e3ab0c-dce3-3b17-84b8-f7b8b1e5c2e8 | -11.8937 | -47.6099 | 2026-09-18 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 43a8d2ec-775d-3eeb-81a0-49a142cc6564 | -10.3769 | -49.9723 | 2026-09-18 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f6c5cc0f-cec7-313c-944f-a66e4d6182c6 | -14.1547 | -45.1442 | 2026-09-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 4e7e2523-c4a0-3c18-85d1-4b4b601ea321 | -9.9133 | -46.5846 | 2026-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 52bd8c51-2267-38cd-be28-0cd176e9ac75 | -2.4814 | -49.4208 | 2026-09-18 14:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 87c2c68d-efd3-3eb7-878e-28b7561369af | -8.9141 | -45.0003 | 2026-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b4923315-d750-3264-b871-8af31d3eae10 | -9.769 | -46.0841 | 2026-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 728cfdf4-15ef-36b8-a0b7-d314660f3137 | -10.2821 | -50.0035 | 2026-09-18 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6126e42d-17c3-36ff-87ff-52361c0cd54f | -11.083 | -48.2875 | 2026-09-18 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2bc16e04-f5be-3469-850a-0eb1d4163cb5 | -14.1542 | -45.1675 | 2026-09-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 677e4397-850a-3f5f-81c4-ef7df915e8b1 | -11.8115 | -46.8158 | 2026-09-18 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 29941f5f-3130-3450-9bba-05b9debd04e2 | -6.3286 | -55.2877 | 2026-09-18 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e5a98e41-7b8e-3395-8d21-a145081826f6 | -11.8556 | -50.0006 | 2026-09-18 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| e1fcf203-c135-3191-9bf7-f1a2d66c7abf | -11.3835 | -47.3206 | 2026-09-18 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |


[Clique aqui para ver as próximas entradas](README103.md)
