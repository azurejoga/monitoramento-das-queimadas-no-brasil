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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b89a6321-875d-3656-85fc-556f25b88ad1 | -10.6726 | -50.4758 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| a1968135-0641-30c9-9f94-5e4e2330390e | -11.6423 | -51.5819 | 2026-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f2715dbe-a6e2-3433-a21e-489d77f346ce | -11.0636 | -48.3118 | 2026-09-18 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 214af774-ccb8-3b16-94aa-bf0c1ca72eb9 | -11.8937 | -47.6099 | 2026-09-18 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2c2185cf-9365-3b7e-ada7-6d6445e7722e | -9.2417 | -45.9185 | 2026-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5cae56e7-d9ea-36ef-9938-c8ce71b97d2c | -12.5345 | -47.0738 | 2026-09-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 189ef2a6-16e3-3a59-8707-531e0d341c1a | -8.1683 | -54.8037 | 2026-09-18 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| bff2751a-0c4d-3c80-966f-9efd567dab0b | -13.2485 | -46.9226 | 2026-09-18 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 0bb85a85-4bde-3ad7-9bd4-04efdba3a1be | -12.998 | -46.9381 | 2026-09-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 988d339e-160d-39ba-a830-b1a1c26afe19 | -11.875 | -47.5902 | 2026-09-18 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e0261d62-9775-35b2-b00e-9c99861386a3 | -11.0048 | -49.7325 | 2026-09-18 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 12657732-cf39-3c29-aaf2-bcdd0bc2cc2a | -14.1542 | -45.1675 | 2026-09-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 299.4 |
| c77941e7-85c9-3ffc-884e-e0c77e9166b5 | -11.2979 | -43.3614 | 2026-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 9cca58a3-62a4-320b-aac8-55b9e0d23342 | -8.6817 | -45.4359 | 2026-09-18 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 29904c69-ebcc-3d69-9f67-75e68753b14c | -12.0461 | -49.9992 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c56ee737-b6ca-3c39-bf49-0dc761153a7d | -6.2949 | -41.7785 | 2026-09-18 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 2fff7864-b0d9-3c3a-8411-66d3d345e973 | -10.6187 | -50.268 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 59e3dd24-5992-318b-99df-c1618b5c925f | -9.9768 | -50.2694 | 2026-09-18 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ff24a843-fdd8-3bac-a144-f1481ab8f31a | -12.0086 | -49.9606 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9008e97b-115a-3a79-89d0-d4be5e521b12 | -12.55 | -50.7117 | 2026-09-18 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c06c8d48-4763-339d-ad85-ba558f73d23d | -9.699 | -54.8176 | 2026-09-18 14:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f8916463-3616-3791-ba4b-8fa2f8210f90 | -6.745 | -45.483 | 2026-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5985696c-64ed-3a63-859e-ad2b43a61a9c | -11.0643 | -48.2678 | 2026-09-18 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b1a25a0b-5206-37ec-b130-a7b4ce4d0595 | -12.5341 | -47.0964 | 2026-09-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 663d1a9a-9e45-325f-88b7-dc1c1df9ff54 | -14.7105 | -50.314 | 2026-09-18 14:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4b5fbda2-95bc-325f-a78a-1ae403b9b88d | -9.8313 | -48.4073 | 2026-09-18 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d616ad87-2f00-3e96-a038-47e4edd968da | -11.8359 | -50.046 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 641f4984-bed8-3a8e-823c-a2b93c3bfe3f | -10.6376 | -50.266 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 267a62a9-b396-3a79-8349-c736748d92c6 | -10.6944 | -50.26 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| c58509be-20fd-3f60-9f10-6c70a5a65036 | -10.5178 | -46.7366 | 2026-09-18 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 93fbfd61-7e22-3caf-9762-43b5f958f991 | -10.3769 | -49.9723 | 2026-09-18 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 48f701e6-91b4-3325-a53d-0050cee5cdd9 | -12.3954 | -48.4727 | 2026-09-18 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e875c345-77cd-36c4-8a63-e892b229e6e1 | -11.2787 | -43.3643 | 2026-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 712654e5-f60c-32f6-9d72-e051d24f3a09 | -7.841 | -44.8614 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 263b3daf-732a-33bb-9b58-ce2dcf1979df | -14.1737 | -45.1641 | 2026-09-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 0b2be869-3512-3f94-9d70-8a96947601f7 | -10.3116 | -45.3136 | 2026-09-18 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3ce66142-7db0-38f3-abed-4362839603d2 | -15.6752 | -52.7339 | 2026-09-18 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fbc3487f-9c8c-3df8-b464-db4a4bd1edc0 | -4.596 | -42.9734 | 2026-09-18 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 288.6 |
| 3fb99e5b-1242-38d4-8485-c7d008e7fd12 | -2.6966 | -57.6084 | 2026-09-18 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 57630fbd-0959-3573-9df2-c8472691f131 | -7.8216 | -44.909 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 79be15b7-eb07-3d78-afd8-c78c7ab1566b | -5.915 | -53.5168 | 2026-09-18 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f2f0ebca-6a3f-3095-ae59-98239fce050b | -7.6346 | -44.8129 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 81bda70e-b4c8-3808-9b6b-696402eddcca | -6.0194 | -51.81 | 2026-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 868f0a05-c8c6-3d55-895b-817f7ff3d0f1 | -10.82 | -50.2 | 2026-09-18 14:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6dae50f-36bc-3436-b70e-8f53e82a4915 | -4.58 | -42.93 | 2026-09-18 14:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dcac771-8141-3e93-8fa5-d921b1d8b844 | -4.58 | -42.97 | 2026-09-18 14:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30e12b6d-be10-34d6-b1ff-8cdfccce0733 | -2.4815 | -49.3996 | 2026-09-18 14:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 637c4e30-a35a-3bc4-b99e-eb2e4b0bcd73 | -14.7105 | -50.314 | 2026-09-18 14:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c0dda6cb-53ac-3b22-9265-65a0faba5c51 | -8.6817 | -45.4359 | 2026-09-18 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 902f4cac-7ab5-3bba-bd8b-a0e17ec207a7 | -11.0636 | -48.3118 | 2026-09-18 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 94028c6f-2ced-306e-85df-18868660e23e | -19.5545 | -47.6113 | 2026-09-18 14:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 135.6 |
| f2e4e730-d792-3fb2-8ca8-2f7801f286fd | -11.8746 | -47.6125 | 2026-09-18 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7e6394db-bdc6-3ccc-bfc6-acaee9cc7311 | -11.064 | -48.2898 | 2026-09-18 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9dc8d46f-b609-3dc0-a6b0-b31be05aa441 | -7.8033 | -44.8651 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3d4dcf46-5ae6-3f03-b454-69f9951ed1d3 | -12.5504 | -50.6902 | 2026-09-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 3762a150-23f3-39de-b5d0-b94b0974d62c | -11.875 | -47.5902 | 2026-09-18 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0cd40102-9308-3fd3-9c2a-747d63b180c8 | -11.0048 | -49.7325 | 2026-09-18 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1bf91eae-e881-3dee-a512-451a73843d3d | -3.7333 | -54.6499 | 2026-09-18 14:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7f5306c2-d9d3-3290-a67f-89cb007cc6f7 | -14.8026 | -48.5622 | 2026-09-18 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8ad76513-b65e-3b40-b599-8b6f46f7ec22 | -12.5345 | -47.0738 | 2026-09-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 1dccb870-4143-372b-9bbd-bfe2a0a08314 | -7.8219 | -44.8861 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c307f950-4135-3537-82e9-2553ca1f362c | -14.1547 | -45.1442 | 2026-09-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| c8444494-559f-31f1-9da8-89ff7ba79055 | -11.2975 | -43.3851 | 2026-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 268.1 |
| 7cee4dea-1c81-367f-8c2d-c15d3d379617 | -11.2971 | -43.4088 | 2026-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 94c0f661-71e5-36ef-82e3-ba4ab477c989 | -7.7844 | -44.8669 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 933a37e6-0289-30d8-a575-78ab062c4e9b | -6.7776 | -47.8981 | 2026-09-18 14:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d4c7eafa-f5ee-3539-a05e-909c182299ad | -4.596 | -42.9734 | 2026-09-18 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 74bff55f-1b90-3f64-98d5-5ebeb6074cdb | -13.2485 | -46.9226 | 2026-09-18 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 5b995b74-be73-30d2-b16e-332f696817f7 | -8.9138 | -45.0232 | 2026-09-18 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f303f639-1d5c-3b4e-abfd-ee85d2495e2c | -6.3102 | -55.2686 | 2026-09-18 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 35c7ef79-2ab9-3c8c-828d-acdf76fe5b5d | -11.3809 | -44.0788 | 2026-09-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 429e6d28-e1bd-33a1-8591-db07a98967c1 | -14.7299 | -50.3112 | 2026-09-18 14:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 30768c67-ee0d-34d7-a083-a1518392b132 | -10.5963 | -46.5699 | 2026-09-18 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 283.2 |
| 10baa79c-570c-3194-bcb0-f1393d57ffc0 | -13.4694 | -51.8563 | 2026-09-18 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 051fbeef-ad73-3572-b3a0-0d1d09bf20bc | -11.6423 | -51.5819 | 2026-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| db9c91c5-6a30-3388-97f3-ac33d9cd4d60 | -11.3433 | -44.0376 | 2026-09-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 47b2a288-006e-3041-b3af-f258f1bde011 | -11.3617 | -44.0817 | 2026-09-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4c865fa4-c61e-3cc7-bbb1-42cfc8f1a87a | -12.5153 | -47.0766 | 2026-09-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a30a3575-1b25-39eb-aea8-ce54cba2cacb | -11.8937 | -47.6099 | 2026-09-18 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 80347384-1365-3a78-ba76-728cdc3f309c | -12.3954 | -48.4727 | 2026-09-18 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5dea2a1d-97ea-30b4-9bf2-0d986f20812e | -4.1389 | -44.2506 | 2026-09-18 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 616c1f80-0fde-3726-983c-20b675ce08f5 | -11.8115 | -46.8158 | 2026-09-18 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| ad4283cf-26a8-3362-a374-b6472bc69fbe | -10.6944 | -50.26 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7e359f5c-a670-3eba-b82f-49fa05ccaf3a | -11.2979 | -43.3614 | 2026-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 66d66fee-553d-39eb-8706-7de14507cf20 | -8.114 | -45.6301 | 2026-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 441adba9-8980-3eab-a804-7fbc4105e70d | -7.8036 | -44.8422 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 0bd8de05-5e38-3d02-bc2e-acff1f3080da | -10.6758 | -50.2406 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 5deef56e-f5d1-3d18-a464-db207fb1a07c | -11.8362 | -50.0244 | 2026-09-18 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 098d3fd7-69a7-3a5f-aa56-865b68c2adf6 | -7.3752 | -44.4708 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3e365cf3-8b46-33ca-8bf7-088f8eab0c06 | -12.0086 | -49.9606 | 2026-09-18 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 0e92497b-22e8-313c-8ce1-ff51f048137e | -8.6646 | -45.3013 | 2026-09-18 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 666b147f-459b-3da9-86bf-c46f1aa0f538 | -10.6376 | -50.266 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5c66e6fa-64aa-3598-b0fc-a73b06a90da6 | -7.1033 | -43.571 | 2026-09-18 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 06c4401e-1886-32ee-961d-085273868a93 | -9.238 | -46.1894 | 2026-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4cc84c09-5dd5-36af-9c87-0938c5073b9b | -12.55 | -50.7117 | 2026-09-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 170.7 |
| eeda3135-9aff-3eb3-a5c9-03e2e178738e | -10.5178 | -46.7366 | 2026-09-18 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c207a618-8c4d-3c99-9a07-fea79d6ebd2e | -13.6341 | -46.9304 | 2026-09-18 14:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4f6c3926-0ea5-3aa3-900a-5576bb79349f | -9.8505 | -48.3834 | 2026-09-18 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| dbffcba5-cbc7-3c69-926e-b6084e125290 | -2.0769 | -56.4085 | 2026-09-18 14:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b3dc55e5-a596-3485-89a3-e9c6b31d14de | -15.6117 | -56.5537 | 2026-09-18 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |


[Clique aqui para ver as próximas entradas](README101.md)
