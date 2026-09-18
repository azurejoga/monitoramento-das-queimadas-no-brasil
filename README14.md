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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca58b751-9dec-3604-9aa8-fee9ed3dec44 | -10.6387 | -50.279999 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 049ac637-0b1a-372f-ac7d-28a1a2b7b04d | -3.9573 | -56.131901 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4e1355-a0ed-3f2b-bd39-68db2b599dd6 | -11.6674 | -54.464699 | 2026-09-18 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e428fa6-bcd8-306e-92cc-35b5ceac543f | -3.9196 | -55.921501 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610ae5f1-c978-3597-b4d5-97c44fefba38 | -12.3499 | -50.7388 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 660dcac9-4c25-31f0-b556-6f4cee5e7ca1 | -5.7491 | -57.5868 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19e15cbe-53ff-36f3-8b39-749b324433b4 | -28.348801 | -52.189499 | 2026-09-18 01:02:00 | METOP-C | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c05f266-6b51-36d4-9f59-06af7511d4f6 | -19.553699 | -47.629902 | 2026-09-18 01:02:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66dab17f-de09-304d-a151-b2f8a7fdff18 | 1.2527 | -50.780701 | 2026-09-18 01:02:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 806a95d3-a2e8-34d2-a7bc-a6b35b0b9984 | -12.3535 | -50.754398 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed5fa55-c902-3e0f-9e8f-3c0f3c930b4d | -2.5663 | -54.7444 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86b72d37-2ca8-3acd-8951-9dcc877e6aef | -8.9323 | -50.925301 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1659e3cc-6f51-31c1-8d6c-d5182066f436 | -7.8241 | -44.911999 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 962a8372-a396-3332-9be2-105b740e6a82 | -4.6038 | -42.999599 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8c84772-7881-3a8f-8d2b-99c458fc29c5 | -13.2471 | -46.908798 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b15fb7b-3dcf-3bd0-9b93-195bf28785de | -12.4681 | -50.8899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdb02532-cdcc-3d54-a567-7fb7fd17e135 | -12.4384 | -50.676102 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87291985-6d4f-321b-9c89-dc59759edb59 | -9.9544 | -46.606098 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79383753-dd3f-3767-9a3b-aec33faccebf | -10.8338 | -50.188099 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54708e43-27ee-3b96-b6c9-d3a98aaa4712 | -15.6596 | -52.742298 | 2026-09-18 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe58405e-2147-3121-b68a-0de14afd1be1 | -5.3703 | -56.045601 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ba96ec-4b8a-30df-b753-bb5aaf8bab2a | -14.7066 | -52.445499 | 2026-09-18 01:02:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1cafc842-3a80-3643-bcf3-3336c71cd30a | -12.3853 | -50.713799 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dd820ba1-7ec6-309c-ba8d-092a7fd01bf5 | -4.4295 | -55.446201 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eda8d6a-1d36-36b6-a312-0e7f579cfb93 | -9.7838 | -45.0443 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28786c9e-9ab2-365c-a438-dbb1c10af9d4 | -5.7616 | -45.123001 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2326447d-11a3-3b69-8709-b407bd253b6f | -9.7741 | -45.046799 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba860e61-ec1c-363c-aba3-a35b573c0677 | -9.7791 | -45.025799 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11a9d9f3-1540-37a5-94db-525765627489 | -10.8065 | -50.203602 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4c2b75-e3ec-3915-bfad-6de86aceed3b | -16.402399 | -49.948898 | 2026-09-18 01:02:00 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba714f46-c769-3710-aa99-3c2bb4335754 | -12.2912 | -50.752899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94892d63-f1f4-30f0-a5bb-fae34e5013fd | -5.751 | -45.080399 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c04c05b-8957-3f50-8b7a-9e74065f5c70 | -1.0354 | -53.743 | 2026-09-18 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1e3c595-134c-3bdf-9561-2ff722844eec | -5.8929 | -49.7826 | 2026-09-18 01:02:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ee537a-47fe-31a9-872d-82a62f550c73 | -11.674 | -54.4482 | 2026-09-18 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6c6f06-339c-3a70-aa5a-4f1bdbb419eb | -9.0005 | -50.170601 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c19fc403-d9bc-3823-8b5c-8063d21fc407 | -9.4882 | -54.483601 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a45cfe6-b004-37e0-8b02-432aac2e156a | -5.8747 | -53.5672 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3bf045b-dc16-333b-bb24-a167e00d6606 | -12.2697 | -50.749901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e21ff7c-c5c1-3ae9-a898-2b8b7f2326d8 | -4.4926 | -55.496899 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c28aa0-127b-31d2-8235-f83621c0d096 | -12.3718 | -50.7005 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c7d4ef0-8d60-363b-8f76-8978acc9eaf0 | -11.2877 | -43.381699 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85cf1981-5c05-32c7-b1dd-36a67f986e2c | -2.0548 | -52.178902 | 2026-09-18 01:02:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba5b15b-f7b4-3bbe-bc51-e0830255b15d | -12.1772 | -46.976101 | 2026-09-18 01:02:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6de76462-c264-37d0-9625-b730b200d96b | -5.1422 | -55.948601 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f34b4e92-525a-31b4-b2cb-129d82d3d572 | -12.4439 | -50.6996 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76d3edc5-8631-3135-8ae8-a7ef3de1af53 | -12.4421 | -50.691799 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38f5b74c-7fe8-31d4-b94e-06de3a439990 | -10.4039 | -46.627399 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f3b9aef-2a2d-3972-a962-323ecf27a446 | -4.3862 | -55.032299 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccf12db-14b9-3c26-a2c0-ac2810331f2b | -12.6354 | -50.898102 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63bb19dc-f90a-34e1-b6c4-0dfbf0212440 | -13.6034 | -48.298302 | 2026-09-18 01:02:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 568f8587-bc03-3424-8a6c-70af115ecd3d | -5.8634 | -52.055401 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17fda038-5322-3912-bf90-345108db8128 | -11.3188 | -46.7714 | 2026-09-18 01:02:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 685e0e89-65e7-396b-88f9-3c825b2bca9d | -6.6199 | -44.216499 | 2026-09-18 01:02:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 545c8d01-f774-300b-827c-336807c07352 | -2.695 | -57.6008 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 250d5224-fc44-3824-a48c-6627fe4afb68 | -10.1138 | -45.647099 | 2026-09-18 01:02:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 954ec210-266b-34be-9d56-7a8104fa8814 | -10.8163 | -50.201302 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2466b790-f744-3768-8ee5-e3e2bae39867 | -14.1343 | -48.733101 | 2026-09-18 01:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d83a550c-b47b-341d-a49e-acdb75f4ee05 | -7.3518 | -44.631802 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3419c76-1510-318a-ac98-26b085f43be6 | -6.1307 | -59.9534 | 2026-09-18 01:02:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 843e4c23-4e79-31dd-a1a2-f6f8832e209c | -4.4256 | -55.5191 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2013df-aa30-3a74-8f95-00d8a684c605 | -12.4461 | -55.008202 | 2026-09-18 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98a16143-e849-359e-bf55-285344217ceb | -8.8594 | -46.973701 | 2026-09-18 01:02:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d6182e3-709b-33bb-8db4-fcde084dbc1e | -3.4658 | -54.708099 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6e38f0-076c-3d33-b032-0469f8e5b57e | -10.666 | -50.2645 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 540b8ee9-3054-36de-9d25-1182d8fd04e2 | -12.3913 | -50.695702 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2a20a2-ff51-39e9-bfee-f74437d9b930 | -17.7736 | -46.4809 | 2026-09-18 01:02:00 | METOP-C | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 27ade8ab-e2bb-3b85-aeec-d02f7f3941b6 | -10.6571 | -50.487202 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 707501db-47f7-33e4-8659-29bd3b8f90b1 | -3.474 | -54.699001 | 2026-09-18 01:02:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b48a49-eeba-3743-8c36-f4246d8c432f | -21.042101 | -48.473099 | 2026-09-18 01:02:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1e02ceda-1cc1-3722-b6f8-82548889d805 | -12.2619 | -50.759998 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87e50906-e192-3bc1-945c-a97da0e95a4a | -4.5112 | -56.0746 | 2026-09-18 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07f7df92-a592-3901-91ad-6a98f5586a84 | -12.5408 | -47.1054 | 2026-09-18 01:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e43d1fe6-f746-3be8-8a66-6441fe4bcbc1 | -4.5369 | -54.9697 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961f99dd-227c-3460-99f8-4f34d43fe24c | -12.2948 | -50.768501 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1eac57b-91ee-3e07-83ff-74a3a26d75a4 | -4.351 | -54.7892 | 2026-09-18 01:02:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf9eec2-c193-3321-8285-6b39a2afc133 | -11.3357 | -43.3685 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7be0136-eed9-3d35-9d66-48aa736ca2b6 | -4.7683 | -55.7103 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e72831a-f125-3554-89b9-80068f41884b | -10.8749 | -54.008202 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08bfb148-3f79-377c-a349-f4b12871b862 | -2.8925 | -54.190701 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe5e0a3-2680-3878-834c-546b8c8f7c0c | -12.348 | -50.730999 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c227cb1-f424-3cf1-b0aa-fb112b14e7c4 | -11.2817 | -43.3591 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 459c576d-7e83-3b21-b685-1fc510275f94 | -12.4659 | -50.661201 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 760fe0fd-ec8e-366a-9585-caf365e899cc | -12.3401 | -50.7411 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d24e1fe7-bfa6-397f-be20-0e42b7b3146d | -5.9026 | -53.509201 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a256a401-3c7d-32f0-92ff-1d91dbe1e7fe | -10.9961 | -49.744301 | 2026-09-18 01:02:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3aa76362-751c-3f89-9615-d44fb123da6d | -9.089 | -45.7145 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d94ed80a-f59d-3f82-835e-88e004982c55 | -11.0205 | -54.151299 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25551f57-d7b1-3fdb-9144-e24e5f03a830 | -3.9589 | -56.138802 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06992753-9a29-3679-9440-ac3f35787e5d | -12.3614 | -50.744202 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43a65ddc-9587-3269-bc31-14a7c10ff2d5 | -10.994 | -49.735401 | 2026-09-18 01:02:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 501cb6c2-94c7-3dfa-8eb4-9bcab8b9472b | -3.4756 | -54.705799 | 2026-09-18 01:02:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427a8fa1-a75a-32a2-bd70-39477fa666a0 | -3.4302 | -58.207199 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac8640e-7476-3db0-bf4f-af43f75ed8a7 | -21.616699 | -50.016998 | 2026-09-18 01:02:00 | METOP-C | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ceb5ef8b-51bc-30ad-b1c1-3bc26753c2b7 | -4.5389 | -54.933498 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb5e93a3-5c9f-3bb6-a9f8-0873a65cf187 | -12.4548 | -50.8769 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58305d27-a9af-3f1e-8383-7c80f6c5fdc8 | -4.5847 | -43.004398 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a318a99a-0f74-390a-a5ab-346ae8891a1e | -11.3092 | -43.423901 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b20b973-8fc6-3c29-af7c-3861b0d0eb31 | -6.0154 | -51.779099 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e1c206-18db-3bf8-8e86-85e6c7e7bb48 | -4.3878 | -55.039101 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
