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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e3e1bed-287c-35ac-91fc-55691be80462 | -7.17354 | -44.80555 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b2eaa597-5c1d-34af-9179-bec9157f54b3 | -8.67063 | -63.98756 | 2026-09-28 17:09:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e6fcb06b-9815-3d25-bbb1-53786147c23e | -10.9106 | -44.65535 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3c64f5cd-2df2-3f16-a8da-80751cdea3a5 | -7.7018 | -46.96516 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dda96652-739b-3dd3-aee2-91cfede2d1a8 | -6.21342 | -52.90753 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 519c6393-d2c4-3685-8629-616d4f662bc2 | -6.23618 | -46.56139 | 2026-09-28 17:09:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d848de4c-f1a9-3ccc-b8d3-0efe378b7786 | -8.57542 | -45.76248 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3ce0a09b-1ad6-3c14-995f-3d01b9bba3e6 | -12.79479 | -54.01774 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| b962b7ed-3746-3b36-b4a9-a35e10edee11 | -7.26694 | -46.92467 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d99c9a28-f996-3706-89b4-bdb4991f2dd5 | -9.50734 | -46.35759 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1a8dee76-d300-3633-be4c-18f9f72e4f4b | -7.27638 | -44.31003 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 33b175df-1f47-35e4-8df6-b0ed6b12d74c | -7.23025 | -44.85518 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 269d6afa-758e-3cd7-894e-6115bf554ae1 | -8.1036 | -44.00778 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 575f121d-15e3-309b-939b-a5d80677b0e4 | -9.33016 | -45.38219 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a38545df-6775-3c10-9711-ae470403cc8a | -11.436 | -44.93051 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaa64878-1647-34f2-aa23-fb0c93dc26fc | -9.51345 | -46.36264 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb20a2d4-7e97-3cde-b40d-44a86090b8c3 | -10.25173 | -44.60036 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25fd28f2-7f93-3cb8-ba41-f0d1f5977414 | -11.16244 | -48.47282 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6156f8f4-7952-3fdb-bd1f-09e1bb581927 | -11.52879 | -47.39248 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 764b8623-708f-30f4-b976-45b5be4f46e1 | -8.19279 | -50.15985 | 2026-09-28 17:09:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ae069bc4-78de-3ee4-9c2a-d336ddbd9f49 | -10.75198 | -54.08356 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bbbae04e-b78a-31f1-9e04-3dc8f86f65dd | -12.14625 | -50.37281 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3f555390-8c63-38a5-9fab-96cebb2180ec | -11.21564 | -44.79364 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e932d6ae-f1bd-3420-aa44-8d477fe1d7d8 | -10.27431 | -44.62927 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| aa6ee14e-aa16-3122-8640-7184cbdeb719 | -11.18737 | -44.82155 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bf1c3926-aa00-3dae-96db-369d30ba4a82 | -7.67874 | -44.88594 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e8842a44-9fad-31f1-a815-4d095859dd30 | -12.07522 | -48.53981 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10ac5df9-7fe4-3918-9533-851a18c8344b | -11.87898 | -50.89505 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 8eb618c5-2c69-356e-8159-94fd998e1c02 | -9.59588 | -49.64256 | 2026-09-28 17:09:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee9b80db-0dde-3828-913a-ea837a71cbc4 | -8.51482 | -46.9001 | 2026-09-28 17:09:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd336ab4-24b4-3018-ba81-bf26e82e6039 | -7.43333 | -55.63642 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 54884f79-71ff-3d9b-ad02-95789df8ee39 | -7.27183 | -45.336 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d2b8e3bb-608a-3318-bdd9-4404e2fb131f | -11.8543 | -50.90369 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 91dcdaf0-f4d2-3dd2-83ff-dc329bab7433 | -11.13038 | -51.18033 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 846ac3fd-ac5c-3857-b0c4-765df4ef4b41 | -5.65081 | -44.23042 | 2026-09-28 17:09:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 929a98e1-4533-32a1-9405-b766547753e0 | -11.12896 | -50.06975 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 71a3f71c-8e8b-3bd4-8425-abcdda53fb4a | -9.29567 | -46.44057 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 481bdad2-8a89-38ca-94fa-3ab61401a979 | -9.11728 | -49.90877 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ec9a4292-d1c6-3b65-904e-02ee20cec5fe | -10.49817 | -43.49202 | 2026-09-28 17:09:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| aebba9bc-0158-3f01-adce-ad4aa6d32962 | -12.59232 | -51.95955 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e36868ad-c2e9-3926-be68-bf5f9c003379 | -10.9458 | -50.67749 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd6756cc-e463-3f8e-a178-b70d8a14a67c | -7.37261 | -41.78577 | 2026-09-28 17:09:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 3c94b1e2-211f-35c8-b358-0c0f4de95cdc | -11.17727 | -44.79797 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| c81f96b0-0d83-39c7-85a1-9c2947436249 | -7.45855 | -64.33143 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| eed48d7b-aa22-3354-8e30-5b8ce6a5361c | -8.23521 | -54.69611 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 112f1603-93c1-3c43-a404-18dbb843ab22 | -7.12955 | -47.60544 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5841ccde-ac9b-359d-911e-edfd9b0931ef | -7.82691 | -55.13713 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3910f7cb-121f-3341-99f0-f1487f1a32d4 | -6.1459 | -53.12557 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00c9705e-5648-3d08-8365-e40f11320307 | -9.67688 | -45.56961 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f29c564-ea9d-3687-bb16-f3a82e66f8e5 | -12.78818 | -54.01879 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 02738f49-7236-3a11-98e3-e6e18b3292e6 | -8.59713 | -48.37128 | 2026-09-28 17:09:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5a23d9e6-b114-3efc-a92a-d0f43b47f47f | -9.49219 | -46.35611 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b7c6e44f-9aea-35e5-9715-ccdf13299774 | -9.96547 | -51.4482 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d078179f-43b1-3e09-8a9b-cafe8b2ac075 | -11.59322 | -65.13448 | 2026-09-28 17:09:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5c9749c1-99fc-3987-b729-79f76ddb6e58 | -7.68401 | -54.84801 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6dea25a9-2cf5-316a-995f-4ea5c7b1888f | -13.51203 | -61.13067 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 43e4b5e4-4118-3b2f-a629-5bf4084998ac | -5.22903 | -50.47935 | 2026-09-28 17:09:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e0026f15-2660-314d-a1a6-3d076cc4b857 | -7.71236 | -44.89908 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14f34816-76d6-359d-94ab-aff7b87838bc | -11.98417 | -57.60503 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a6a5cd90-c2be-355b-b2c7-40a333da919e | -11.52622 | -47.38536 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 4e67002a-a5d7-3cb9-a124-107af96df3ab | -10.891 | -50.68053 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7daf729f-5a1d-3030-9379-ab6289db9429 | -8.19222 | -50.15636 | 2026-09-28 17:09:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ebd3a1bf-2508-3f8b-af3d-f30a9869b792 | -6.92006 | -55.61082 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e843612e-a10c-31e7-9763-fed6198bc6b3 | -9.93516 | -50.22895 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1a8dc370-5011-31a5-b805-a39a2b1d5e7d | -10.21498 | -50.02063 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e0502713-9cdd-3a4c-a1a9-56ac7528ff13 | -10.16343 | -43.90053 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| eae35f5c-e528-3fe7-a0ee-69cd2d3f11a1 | -10.84401 | -61.42714 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9be241de-451a-3d5f-867c-f860c08b80cc | -6.13146 | -53.05611 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6afc7650-b528-3197-8c44-ac7c9eccd8dc | -8.27892 | -54.7137 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 742ade88-fc3f-3bd5-ac80-95eb9335411c | -11.21226 | -44.77571 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b6ddd7ac-8a7c-3f78-8050-aa035d3045ea | -9.07614 | -47.18831 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30cb4192-d713-3655-8b29-06f9a4acccd8 | -7.67948 | -44.89008 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 3e813b74-af4c-3a98-98cd-1af26d0a4448 | -12.147 | -50.37734 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 031969fa-31a3-3525-910c-864cce75b6c1 | -9.48683 | -60.39721 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ff58aec5-aa77-3f28-a1b5-2210d852f36c | -11.19412 | -44.79824 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 86ceb8fd-6b12-3605-be44-d7fb3779d126 | -5.73276 | -45.01178 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79d65693-3e48-3fc7-9d05-40ee65d30b23 | -11.45729 | -49.73898 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 57c806ba-369a-3247-a950-3bbdf8bc8477 | -10.70401 | -50.83002 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 717963eb-fdce-3ff6-b939-f3948c133910 | -12.11824 | -57.16444 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5680fdd8-9f12-3530-8d6f-c82208c1ce38 | -11.17499 | -44.79518 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 70279415-1517-34be-88a7-a2f9f681b3b9 | -7.84592 | -46.93513 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 46875b0b-c804-37b7-82b0-9973f465ed3d | -10.95546 | -50.68972 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 28696f25-2aad-33e6-9579-66b73e1cb3fc | -10.95738 | -43.87877 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2bd33a27-a2c1-3a22-b373-21a2e46b731f | -10.95917 | -50.68908 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7fdacc41-bf9b-355e-86ed-ad7f3cdafe4c | -12.05911 | -50.21852 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7685c1b1-6148-3abd-8547-00ecff852082 | -10.7057 | -48.74855 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 32bd2a45-bc07-3634-b4e4-6b50bf3210f7 | -6.19629 | -53.22864 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5e492a7b-dd55-3f95-90a8-a780a0222730 | -10.8265 | -60.73091 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 153f04f5-5f42-3f8b-8936-2420b15ded6e | -9.39982 | -46.3906 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 22aa1221-2db3-379b-b98d-c0e2de8cdabc | -7.72141 | -44.88428 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7011c4c1-2bc5-371d-9116-75774fb92db8 | -10.11502 | -50.19304 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 6913cdae-3e67-3d7d-8630-80f86c93426c | -6.58613 | -49.62598 | 2026-09-28 17:09:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 739df2d5-c301-3bdb-a21c-baced6ebd768 | -9.98775 | -50.13079 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| fa0e9ca4-96a9-356e-a04e-586e91b6788c | -9.0777 | -49.8686 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e994a9c6-390f-3387-8f37-82eaf13467e8 | -11.58519 | -47.02098 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| dd68e00f-61e5-3871-8259-68241b5b1e8f | -11.87031 | -50.88771 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b73197df-ebbb-3f06-9498-7edbbd593bd6 | -8.36204 | -45.39796 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b7f3c493-41dd-3187-8df8-7fe2d45d2179 | -9.82596 | -44.94431 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b07d2cd-90d5-3188-8526-54c0f70aa243 | -9.44188 | -48.93701 | 2026-09-28 17:09:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 00840485-4ec3-3abd-8144-2f5edc5d1a4c | -9.14069 | -49.97637 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |


[Clique aqui para ver as próximas entradas](README144.md)
