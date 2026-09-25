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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63c3ad43-961a-392f-b269-473007c54050 | -9.1535 | -59.4834 | 2026-09-25 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 40efdd95-40cb-31f1-b28d-15f468b955d7 | -3.2314 | -46.9376 | 2026-09-25 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 526a419f-fd56-3806-9a3c-92a8bf7f48e0 | -9.4773 | -40.3116 | 2026-09-25 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 74fcd037-c324-3191-bc15-356fc3d2a5b8 | -11.7849 | -50.9086 | 2026-09-25 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 7225607b-75e2-3d55-b714-d1d9c7dbde86 | -11.2859 | -51.3031 | 2026-09-25 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e10650eb-a505-35eb-8e4a-b67879af3eca | -3.25 | -46.9369 | 2026-09-25 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 3a3511ab-95e6-3386-a2a2-47ee04bb3ac0 | -8.7741 | -45.5849 | 2026-09-25 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| aeed0acd-fca8-3dd3-a28c-c450d1feedb5 | -8.34 | -44.1427 | 2026-09-25 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 99210eb4-312f-3fd3-b182-691df8a46438 | -9.1536 | -59.464 | 2026-09-25 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 22640deb-b60e-3f35-a8ad-2668dacdcfe7 | -1.1461 | -54.0996 | 2026-09-25 02:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 55b40069-8dc1-3920-ab8e-b2ca7bbd653f | -11.3048 | -51.3011 | 2026-09-25 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6da0a4f8-6b8a-33d4-940e-9867b21b4d93 | -8.7738 | -45.6076 | 2026-09-25 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| c31f98ff-3ff4-3ee9-9ea6-2b055873507f | -8.3211 | -44.1447 | 2026-09-25 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0d126ec9-b441-3376-8928-90dfe4494beb | -3.2314 | -46.9376 | 2026-09-25 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.2 |
| d746709b-2b78-3eb9-a933-06d84036b05d | -12.1685 | -50.7147 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0f1fe09f-2e66-3149-9f1b-6da5ea9e849c | -12.1115 | -50.7001 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 326a8460-5e4a-3111-a43e-fbc29d80d0b7 | -12.1869 | -50.7553 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| fd9a0c9b-d4bb-33ce-82c4-5e93279fe1b8 | -12.1872 | -50.7339 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 1279cd57-bd29-3f1b-a0d7-cdffca532c84 | -12.1681 | -50.7362 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 22356241-ed78-37c4-a50e-a8597cedebe1 | -12.1876 | -50.7125 | 2026-09-25 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 25a6f027-c5cc-349e-b038-7a6425b5068e | -3.25 | -46.9369 | 2026-09-25 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 6e94d5b5-7bf6-39f4-b48b-85276da4a202 | -8.3397 | -44.1658 | 2026-09-25 02:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 102f19fc-4577-3a22-8c06-f0936ebebf1e | -9.4773 | -40.3116 | 2026-09-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 76670847-5512-34b1-98bd-99eb2cdf9cee | -9.1535 | -59.4834 | 2026-09-25 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2ff917e7-47de-31a6-8b2f-83567707770e | -11.7849 | -50.9086 | 2026-09-25 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 3204580a-2e46-3139-bb2b-ed8741118189 | -11.2859 | -51.3031 | 2026-09-25 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 316ce03c-fade-3c83-93cb-3f079ba58cc2 | -9.4769 | -40.3365 | 2026-09-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 181.2 |
| ffbd9d7b-6886-3bbf-a14e-63b6e76f8810 | -7.9082 | -54.7597 | 2026-09-25 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9de91812-f24b-3d94-be82-358016a2d2cb | -9.1536 | -59.464 | 2026-09-25 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3ee8cea3-1d62-360d-8aa3-7bf62d129545 | -8.3211 | -44.1447 | 2026-09-25 02:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5d3fc4c6-b9e2-3129-a704-50760ad3ce84 | -1.2189 | -54.5592 | 2026-09-25 02:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f3335f65-a7f5-3f17-8428-04746945b720 | -3.2047 | -53.4179 | 2026-09-25 02:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d730e428-aee5-341b-9edc-8df6d9c0cb31 | -8.34 | -44.1427 | 2026-09-25 02:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| fe086b25-6982-35c1-8d0e-bfa99f6ec2d7 | -5.7754 | -45.1053 | 2026-09-25 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 34076ed8-e8d1-39c5-ad36-2e18746999a8 | -11.7849 | -50.9086 | 2026-09-25 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 05c706e6-0f89-3962-a54b-57b8e16a16cf | -12.1869 | -50.7553 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 281981ae-195b-3f03-a4fd-b4650c6645a7 | -9.1535 | -59.4834 | 2026-09-25 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1c2b3e78-96bf-327b-b7ec-360a2f8fc458 | -12.1681 | -50.7362 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| fd198b31-955a-3964-8817-731c40ecc405 | -11.6567 | -50.5817 | 2026-09-25 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 8c05fcdd-23a1-3e67-b54b-7b0c426f30dc | -12.1872 | -50.7339 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 6b58c39d-bce6-30bd-8e4d-57a567eaee8b | -3.2047 | -53.4179 | 2026-09-25 02:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 51bbb446-9ffb-348a-9c7c-07c8f7e3c075 | -8.3208 | -44.1679 | 2026-09-25 02:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 790ca5be-a7d9-3990-92bf-07b975334a6b | -1.1461 | -54.0996 | 2026-09-25 02:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d6a98262-9f47-3736-9f43-f2b9300286ef | -11.7853 | -50.8872 | 2026-09-25 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4df12038-4747-3622-bff3-18f3406751be | -11.6564 | -50.6031 | 2026-09-25 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 86f9da13-fdc0-3917-870a-9086f5f0d5d0 | -12.1685 | -50.7147 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5fa5dbc8-2860-3417-aa30-3b2503706358 | -4.4098 | -55.5446 | 2026-09-25 02:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| afdf05c3-c32c-368a-8b6b-311f54540f4b | -9.4773 | -40.3116 | 2026-09-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 192e7e72-2f4f-3045-84db-9f80464704b2 | -12.1876 | -50.7125 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 9dd3df77-640a-30d8-b77c-345d7f14f7ee | -8.3397 | -44.1658 | 2026-09-25 02:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4cc3c139-39d2-3073-ad65-475612955809 | -8.3211 | -44.1447 | 2026-09-25 02:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 4c0451ad-8f0e-30aa-8b62-41a6e809f4be | -11.7659 | -50.9107 | 2026-09-25 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 6ae1a040-5daf-310b-af9a-8f4bc14cf4fe | -12.206 | -50.7531 | 2026-09-25 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| cb58269d-bce2-3e66-b884-0a3148052041 | -7.9082 | -54.7597 | 2026-09-25 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 747c5a0e-530e-3ba9-8b52-9d4ea62c418b | -11.7846 | -50.9299 | 2026-09-25 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| dc9902d0-3672-3d92-9f45-ff54e98ad6ec | -8.34 | -44.1427 | 2026-09-25 02:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 65ad9751-a7fe-3fd7-8258-8e81efaf6cae | -3.25 | -46.9369 | 2026-09-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| d80d8582-0e01-3e1c-88ea-6ba39b173b77 | -9.4769 | -40.3365 | 2026-09-25 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 163.1 |
| 7961519a-6306-37e4-904c-ce1b94999fe1 | -3.2314 | -46.9376 | 2026-09-25 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 71b0220b-00d3-3494-a6fe-502857c364ba | -3.2047 | -53.4179 | 2026-09-25 03:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bf0f3064-c497-3662-a27a-51b1b8e5ae5f | -12.1872 | -50.7339 | 2026-09-25 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5d442bfa-de59-3f10-b1b1-390689521107 | -5.7754 | -45.1053 | 2026-09-25 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 2aee4d23-e50c-3805-807f-6811d05611d4 | -11.7659 | -50.9107 | 2026-09-25 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0982dbd8-0f82-3d08-adad-4740988b0cb6 | -9.1535 | -59.4834 | 2026-09-25 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0174a416-a281-3610-aa32-843fb4a21137 | -11.6567 | -50.5817 | 2026-09-25 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6ece4d64-31b4-3477-801a-9524c42b2a11 | -11.6564 | -50.6031 | 2026-09-25 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d699cf5b-6d0d-37c1-9ad3-7bbb22ab5768 | -11.7849 | -50.9086 | 2026-09-25 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f64435ef-8a0e-30f2-9d62-10b94fd32449 | -3.2314 | -46.9376 | 2026-09-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 050545bc-0883-38a2-9f4e-c40159085e9d | -9.4769 | -40.3365 | 2026-09-25 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.0 |
| c41cd4db-1504-3af5-a541-049548fd4dbd | -1.1461 | -54.0996 | 2026-09-25 03:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8fc5f4c9-256e-30fe-9d20-a294c03c6e23 | -9.1536 | -59.464 | 2026-09-25 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 280399a0-9049-325c-ad47-eb983881fd3c | -8.3211 | -44.1447 | 2026-09-25 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 60314768-c351-38d8-bffb-139bf22a472b | -12.1866 | -50.7767 | 2026-09-25 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0af3f198-08fe-380d-a284-29d91cd201d7 | -8.3397 | -44.1658 | 2026-09-25 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d8087d9a-ebf0-320a-9206-98633834b4de | -12.206 | -50.7531 | 2026-09-25 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a61177f5-ed64-3a68-919f-fe7ddfc75b00 | -12.1869 | -50.7553 | 2026-09-25 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a2603992-876c-3eae-b9c1-384174fd8e51 | -11.7853 | -50.8872 | 2026-09-25 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a89f0946-b6fa-3745-88b2-4ecd72f5eed3 | -8.34 | -44.1427 | 2026-09-25 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| ce27e371-6bc0-35a1-86e8-d5f971a0355a | -12.2063 | -50.7316 | 2026-09-25 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bc7c13cf-d7c2-3a9e-a2f0-4c81af8a56c7 | -3.25 | -46.9369 | 2026-09-25 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| f67c838c-9968-37c5-8739-30b60d5d55b3 | -7.9082 | -54.7597 | 2026-09-25 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 49e6e376-0cfe-3d58-a341-52342a81ed18 | -6.29372 | -35.24639 | 2026-09-25 03:04:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 56fd6341-1ca9-3f40-97a4-d4990fb8b754 | -6.42732 | -35.25102 | 2026-09-25 03:04:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7f5c1797-bfbd-36eb-8251-0ad68e87a41d | -11.94539 | -38.29448 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb40bfdc-206d-305f-a761-c98957e5445f | -11.94463 | -38.29102 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e3260d4e-5cd6-3904-9598-b182dd711ae7 | -11.92474 | -38.29534 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| f658d55e-619a-3652-ae35-d6b4d7669a02 | -11.93126 | -38.29684 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| df3c6a3a-e988-3c17-aeb7-32cc22d54b10 | -11.93776 | -38.29842 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99380fee-9822-3f50-860e-e1badd65fa3f | -11.92357 | -38.30104 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8cc1b69c-19e7-3cad-b901-c7b46b3d8777 | -11.93572 | -38.30086 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 68f743e6-bd90-3546-ad15-4584d9e66490 | -11.93694 | -38.29509 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2bf465e0-66d1-3694-952a-0759b943ad3d | -11.93008 | -38.30258 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 06eb851f-015a-3bff-b621-259f2373961c | -11.9466 | -38.28858 | 2026-09-25 03:06:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9cecdfd2-58c2-338c-a5ca-7ea262388441 | -15.51057 | -40.0163 | 2026-09-25 03:08:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| cd918b11-e716-3ca7-a2d6-64e43438aca3 | -9.1535 | -59.4834 | 2026-09-25 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 34ccc6a2-baa2-360b-88bf-5a302492e34d | -8.3397 | -44.1658 | 2026-09-25 03:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bf1e7e7c-86ec-3684-9173-d7206c92904e | -8.34 | -44.1427 | 2026-09-25 03:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 0ef06de0-181a-3fcd-ba74-b14a394f4926 | -3.2047 | -53.4179 | 2026-09-25 03:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2b80bead-3a5f-3f9d-bad5-b8c0c3e0157e | -8.3211 | -44.1447 | 2026-09-25 03:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c6dc8e96-0127-3815-9d57-5d8ea57e093a | -1.1461 | -54.0996 | 2026-09-25 03:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |


[Clique aqui para ver as próximas entradas](README10.md)
