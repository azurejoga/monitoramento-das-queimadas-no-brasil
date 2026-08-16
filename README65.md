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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdef1dca-5105-340e-b65a-59b1b1386a8a | -14.4816 | -53.4598 | 2026-08-16 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 655cb0c8-e219-3bc8-8061-0f1e62430513 | -8.4275 | -62.676 | 2026-08-16 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| fd381948-6d02-3b7c-9087-e5e57465f41d | -6.7122 | -58.9606 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9c0df30d-c310-3cac-8a7a-d95fea99d209 | -10.181 | -46.4183 | 2026-08-16 14:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| b1209fbe-0643-3850-a03d-e62647c17b54 | -12.0095 | -46.4271 | 2026-08-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a5dca053-e274-332d-8145-42254e7ee5d8 | -6.058 | -44.88 | 2026-08-16 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 69240aae-c5ea-3fd3-9eba-c96f528b1237 | -11.9899 | -46.4525 | 2026-08-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 8599be07-cf58-3778-816f-da26ac7d40e1 | -20.3305 | -46.7057 | 2026-08-16 14:40:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1707c7cd-e5b2-3f32-8b81-ac0f73e22072 | -8.9415 | -60.5174 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0b046b9a-fa19-39c5-9a82-4bc66f4cb3ad | -8.9601 | -60.5165 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 8c856a98-0371-3157-a0d5-8986de6b7063 | -6.7123 | -58.9412 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 29528718-6152-3d49-9fca-b4838f980714 | -6.6664 | -44.005 | 2026-08-16 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a7872dcf-8d44-3274-945a-9d8cba744d16 | -6.6198 | -58.9836 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 1893b979-e9ce-3e20-8bbb-9336adead0ad | -14.2949 | -51.9422 | 2026-08-16 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c917ef62-cae6-3776-a5ab-df71e7e70357 | -6.8573 | -56.4137 | 2026-08-16 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 07d791aa-9e22-303a-9282-929d0a257a2d | -14.3326 | -53.1425 | 2026-08-16 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 2f03f933-5875-331b-be66-c876dbffb2cc | -11.8482 | -51.7916 | 2026-08-16 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 45586174-f77a-3fd9-a3ee-46a6ae421806 | -10.2576 | -50.4332 | 2026-08-16 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 4cf2258f-52a0-3ad2-918b-b7e80bfd00a5 | -6.1106 | -57.7425 | 2026-08-16 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1896f1cc-5fb3-3b8e-9491-531a1f5edb10 | -13.8038 | -53.7703 | 2026-08-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 73170962-0f46-3af5-b138-c4d84d7d6dd8 | -6.6854 | -43.9802 | 2026-08-16 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 6b0390e6-35ef-3744-84b0-f1a8224d99e2 | -12.0091 | -46.4498 | 2026-08-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 297.4 |
| 8d3223ec-6eec-36e8-bb91-e1356286c59f | -6.6013 | -59.0037 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 30a121f3-9d29-3fc5-bc02-34ab3281e86d | -8.9785 | -60.5349 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 245d2874-e774-3361-9312-a52e5ad27ee4 | -9.2079 | -59.6742 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2e1b59b7-28e8-3a54-b304-d894061d33bd | -6.3654 | -58.3354 | 2026-08-16 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 91547ea1-d217-3cc9-a310-9efa41c707e6 | -14.333 | -53.1215 | 2026-08-16 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 2791785d-c867-31b1-a688-55bc294029e7 | -11.8101 | -51.7957 | 2026-08-16 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 721002bd-bd39-3b7f-afd6-a6f21d27cb87 | -11.0796 | -47.2702 | 2026-08-16 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 28ea0cec-54a0-357c-ac56-4421930aee3f | -10.993 | -50.5698 | 2026-08-16 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7c5e979e-adb4-317b-b743-7101b8fd4ced | -6.9702 | -59.0078 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| e0aaaf19-15f3-30a4-923a-ec91245667e7 | -6.1108 | -57.7035 | 2026-08-16 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 157cd57d-76c3-3c5b-ae28-e07001c7bd2b | -12.1577 | -50.1796 | 2026-08-16 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| fa368d95-f5c0-3348-8e59-dc7f6255efef | -6.8412 | -58.9746 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e35f01e9-1896-3b20-8e20-06cfa16ac606 | -12.0282 | -46.4471 | 2026-08-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2317ae1d-bf79-3d82-8cb8-faa1c766a96f | -11.08 | -47.2479 | 2026-08-16 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 8f8851a7-6c42-3f4e-9e75-510c2c51b353 | -8.9787 | -60.5156 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 61c59ce8-bb92-3227-b439-9bdd7e3b48cf | -6.6666 | -43.9818 | 2026-08-16 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 99f9c4bb-04c0-3e68-9ab8-f301a8d249fc | -6.82 | -56.4551 | 2026-08-16 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cb9a7b5a-bc0e-3dab-8beb-2556968f5354 | -8.446 | -62.6752 | 2026-08-16 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| eae17fb8-3a95-3dfc-bd22-c2d442c0c4dc | -12.0087 | -46.4725 | 2026-08-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f5fce4ef-b2db-34be-8171-c7aaab47b777 | -9.1892 | -59.6752 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2f05ae35-ea48-33fd-8e79-ca2eddd550be | -9.9245 | -45.8169 | 2026-08-16 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 5302a8c8-411c-3b55-a34d-41bd9e829c34 | -11.8291 | -51.7937 | 2026-08-16 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 211.5 |
| dd0e9509-3086-34db-b27e-1bf83b30f38a | -13.7845 | -53.7725 | 2026-08-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c1140603-6762-3488-921c-1280e302607b | -6.8572 | -56.4335 | 2026-08-16 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 03d073c5-22ee-3baa-a6a1-bf50d91f10f2 | -6.6852 | -44.0033 | 2026-08-16 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 33e60bd7-898d-38be-8cad-622b647a762d | -11.0994 | -47.2231 | 2026-08-16 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1d46d14f-fbe3-3350-92af-8ec07c6f4bf0 | -14.2755 | -51.9447 | 2026-08-16 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 59d56d89-43d2-38c7-9c53-a6d6cef202bd | -14.4317 | -51.8388 | 2026-08-16 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| abae26ad-53d8-3cba-a988-37c94ecd52cc | -6.1107 | -57.723 | 2026-08-16 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 5e7acf76-f19a-3bdd-a936-16bb2fe70767 | -7.5871 | -60.8845 | 2026-08-16 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 930f2ea3-f6f1-3fcb-99fe-cd29cdac286c | -6.0923 | -57.7238 | 2026-08-16 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d4a08b55-2994-3742-9797-add53570cd72 | -8.96 | -60.5358 | 2026-08-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 45c85d20-be42-3e9d-8a44-b4f9b810e050 | -8.4461 | -62.6563 | 2026-08-16 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 28978a09-ac73-3834-9a9e-e568c1291423 | -6.8964 | -59.0109 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a4b471b3-fef7-385d-9c12-20c748103ac9 | -15.0677 | -47.0326 | 2026-08-16 14:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a2c9a627-ab4e-3be5-8951-7555633ada78 | -6.6014 | -58.9844 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 96e16762-5196-35a8-906d-05bc05965426 | -6.8387 | -56.4344 | 2026-08-16 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b1ecad82-245e-34eb-a8b7-f2454795e6e8 | -7.7651 | -48.2552 | 2026-08-16 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 076b688f-3a41-3271-b8d0-e6167bbd4098 | -11.0991 | -47.2455 | 2026-08-16 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| bb403887-2a0a-3a31-ac30-d28965ef7881 | -14.4678 | -51.9832 | 2026-08-16 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5246603c-27e2-388b-afd0-0965e2cc0fda | -6.5829 | -58.9851 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| cf2a1728-32f5-3f63-8e55-34049b30f6b2 | -6.2192 | -47.7419 | 2026-08-16 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| faf580ad-263d-3e0a-ba31-9b5078b66a68 | -15.1614 | -50.0722 | 2026-08-16 14:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c369b987-a2c7-3a01-b1b0-650cbca8fed8 | -6.3137 | -43.6178 | 2026-08-16 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6b044d3a-ccb4-3196-9c2e-0eaee447f1ee | -6.7645 | -59.4794 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 9572efcd-f3c8-3dfc-ab7c-9dfd18186cf5 | -8.4276 | -62.657 | 2026-08-16 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 43aad456-d91d-3995-a793-d0d31ea02f53 | -11.4716 | -46.5918 | 2026-08-16 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4e48808c-3ec1-3243-bdad-e6ee5ce39052 | -6.8597 | -58.9738 | 2026-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |


