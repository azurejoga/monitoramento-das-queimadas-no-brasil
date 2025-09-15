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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c569b29b-247c-34a2-a7e0-ba9ab63d33fd | -10.18817 | -46.15713 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 895d4ec0-2b60-36a7-b8a4-bffe34105abb | -13.94633 | -47.94251 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be18e494-7891-3f40-aa41-f6faf1dd7972 | -13.17756 | -47.28582 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdc0ec64-6c71-333a-914c-a71e03129e7c | -15.63199 | -44.38956 | 2025-09-15 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d31308eb-b249-3048-8e20-6d1239b77786 | -11.80562 | -50.43854 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 28402e2c-9dc9-34a5-99e4-fcf414341df6 | -13.11979 | -47.13716 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efe44eaf-f3d9-3637-b749-9877f08ed9c3 | -10.92118 | -45.45281 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36bf4ab4-8584-3291-bf15-1fb040ad537f | -13.93218 | -44.80467 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5b56e67-7e22-3377-9090-3aaa1867c269 | -12.12395 | -44.81704 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2bbba02-9e2e-394d-8d0f-ab002b98a1db | -11.13046 | -45.30989 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0815f8fb-2eeb-3bc7-b6e9-c56ec220a196 | -12.1665 | -44.11979 | 2025-09-15 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 429c7721-66d6-3790-9d35-baad511f787d | -11.81246 | -50.44474 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a0d84fe-6dc6-3295-89d7-743addb67097 | -10.62774 | -46.24257 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70acc564-7fef-3f41-be67-64666946d11a | -14.50367 | -47.33852 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d694351-2178-330f-b488-fb3e49c4b470 | -14.8388 | -45.48622 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2006c0ab-8d20-32b9-b5fa-961eeff4c93f | -11.12661 | -45.3129 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ca23a09-a414-3eb4-aa1a-24de925a931a | -11.8133 | -50.43988 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2a76f515-1cad-30a0-a879-bd67b98f5438 | -14.83435 | -45.49299 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32368d16-170d-3cc3-bb44-93ea3855b33a | -11.44249 | -43.54916 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 951c72d2-19b7-3641-a214-68cb52a24162 | -12.96346 | -47.99644 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d7637c4-f770-3651-b8cd-ab9530f450b6 | -10.74121 | -44.78875 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb58e5ab-6e2b-3245-a0aa-aa12674a8d0a | -10.79437 | -45.98343 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0620e3c-60ce-3512-9878-01bd51f25664 | -11.50887 | -43.64236 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88cc0e70-1fc9-325d-9268-1fc5810e89fb | -10.14716 | -45.37886 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ad80378-86f6-3b93-8b31-ebb865bcc909 | -14.20676 | -48.77324 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72fff4a7-73b9-3966-a727-821a0c5d9125 | -9.11745 | -46.93742 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da6d7d4e-497e-3e13-b187-d7157dd5c289 | -10.76484 | -44.72334 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc148f6a-2fd6-339a-ae15-3d16865f63c5 | -13.19476 | -47.28498 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 70fab3d3-d19b-35c4-9358-463df6d089c2 | -14.17699 | -46.14658 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da4f7266-fd6a-3f26-86ef-cbab95fd092d | -14.50423 | -47.33497 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4237935-aefa-32dc-b246-96da177ba5ee | -9.36046 | -45.38525 | 2025-09-15 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4d54180-8552-393f-8dc6-296378617368 | -10.14078 | -46.1568 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 842ae61a-5c73-38c0-8959-f4a4ba94e65e | -11.86147 | -50.52881 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f5e2fe92-d6fc-3874-8901-9a2dc8aa3466 | -14.2516 | -48.84005 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a81aaec1-b4be-3725-9b0a-cc8429059ca0 | -11.13155 | -45.30285 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f865f06-7747-34c9-9bf7-8eb81613cd8b | -11.85845 | -50.52322 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a0acdb65-6c2d-3ccc-9be1-239c30a46e8e | -12.01074 | -46.66308 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 927daf5c-8a93-3a36-a51a-a2d088c844b3 | -15.07873 | -52.47735 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e09d21b5-37a5-3aae-87c9-3f20ad5d6a9a | -14.33251 | -46.13143 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c77adc-e110-396b-8eb8-379488b5dea0 | -9.54001 | -45.93078 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5ae239-0f54-303e-a911-3e2dbd28724a | -13.94969 | -47.94307 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfcbc7b5-c504-3eb1-ad69-f1bf3301d29f | -10.76176 | -50.6429 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4f1ab09c-18e9-314a-874c-5c8dc9822537 | -14.50974 | -47.3431 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c23c0ec2-80e6-3be0-b8e1-0c3dfaac7ab7 | -14.74021 | -45.28288 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 845d5330-c588-3411-bb05-2c9d3b7bff77 | -10.74391 | -44.77107 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33c51dfb-c943-3587-b7c2-365d132ca83d | -10.74875 | -50.6427 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c069a3f5-0f67-3b6c-968a-adb3bdff38fc | -12.11732 | -44.83806 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8331879-07ce-39c7-b581-b9667e385655 | -12.01792 | -46.66061 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d5d7f9-8f79-3442-b60f-7f7135f7862e | -17.00293 | -45.88301 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6d7adeb-a2bb-3b5a-bf3f-b94e1eff7807 | -10.66247 | -46.23731 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc6eb714-bbe3-3464-a324-68118f113ffc | -12.01736 | -46.66415 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4caf04f6-6c88-3587-8fe5-35d74805f459 | -10.75695 | -50.64736 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67df3d05-fa38-36af-80ee-a90bac28a45e | -13.94179 | -44.81005 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bee48010-fd33-32ab-af04-5d5021e893d8 | -11.33514 | -43.49352 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78df7e40-19de-307c-83f7-7c8801ec7d8c | -12.07747 | -47.56317 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b089311-74f5-3add-a5fe-c300554fdb07 | -13.64557 | -46.998 | 2025-09-15 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d00e248-c26e-3fe8-a11e-811e4d9ff12f | -12.97847 | -47.96841 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d20535d-9237-380a-85e6-6ce3a632b860 | -15.78952 | -52.20991 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96d912a2-7c50-3cdb-b34b-06337d742247 | -12.95879 | -48.0036 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7f6b1ba-630a-3ee0-a7da-d061e80aef1a | -9.01692 | -48.02411 | 2025-09-15 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99f51141-20cc-3333-b9ab-8fff0ccbdcbc | -12.00743 | -46.66254 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 16a4931b-eabf-30e1-bc52-1026ab0c03dc | -11.7756 | -50.43996 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1513e87b-0ca9-3f9a-8fdc-10c9e14b9fc9 | -12.67923 | -47.73455 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ecf83390-b25c-3e7e-b170-72579db23cef | -11.72172 | -46.48967 | 2025-09-15 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 452e2de5-4bc0-367b-8bc4-e25b88fef0ee | -9.01575 | -48.0248 | 2025-09-15 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 284fa8d9-eed5-3eb0-a09b-dae9af2423ea | -9.17744 | -47.04795 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a59b1d2-db06-3412-9339-05cec8346cc7 | -14.63778 | -46.37783 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4632958e-2c18-330c-a756-51082912a0b6 | -10.6316 | -46.2396 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb4be80f-9a6c-3919-bd74-e805d4fba3ec | -10.8656 | -45.46198 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06d254db-ea40-3847-9545-214ea13137ee | -12.96621 | -48.00084 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c68d47db-47da-3762-9373-0d3dd1a83736 | -12.44648 | -46.87658 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2135f223-3d82-3c3f-8c95-4c9f0302db83 | -12.04955 | -46.5465 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39fbf24d-d9e9-35f7-978f-510166be2db3 | -11.24536 | -44.7612 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73fb092a-d9d6-3dc3-9e0d-283b6b157c6e | -11.86066 | -50.52085 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f88958a4-20df-38ca-9659-acad9dc78012 | -11.45464 | -43.56295 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 248577b1-f661-3649-a9ef-df845568b3e1 | -15.79224 | -52.2179 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1eb7a70-fbc7-368f-95bf-fa97e81b39c2 | -11.3138 | -50.85323 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 745a617d-edb5-3b2a-838e-fb5a66969835 | -14.49534 | -47.34809 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6725c58-4c97-390c-a932-0912dee70ce1 | -11.79451 | -46.65307 | 2025-09-15 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85983b24-3b19-3483-aba6-3af0aa620566 | -12.6826 | -47.73511 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e5aaaa2-f77e-3a2a-964f-bdc3cff02676 | -9.84695 | -43.15803 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b3535a7-59a8-3a19-ac61-62ee6f16afe3 | -12.05341 | -46.54353 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761339db-c9d0-3b54-8246-dab21a948eef | -14.50918 | -47.34662 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fffe8b00-9a09-3054-8f43-83109d24db1d | -13.87994 | -48.30409 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaba0085-ada7-373c-b091-dbb8ae43ca5e | -12.12515 | -47.56726 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b584271-0f79-38b4-8153-976eefe34f5c | -14.43419 | -53.36783 | 2025-09-15 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7ac2026e-1b9c-37ee-bd29-1bb6c08799ba | -14.19989 | -48.77206 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac7f4f36-1193-3114-a8ed-12f82adaebe2 | -16.28547 | -45.68658 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05b916ac-33fb-3068-8b8c-d7711cfcde48 | -12.92845 | -47.96851 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4aea58d-06eb-33b8-86e2-c5be9e70991d | -14.40123 | -48.35738 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb70397d-2a4f-3221-950a-1c7b9389d85a | -12.99718 | -47.96009 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89dbf056-d215-3241-8f28-ab947615139c | -16.28321 | -45.67862 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0606825-b0a6-3536-aa21-17f0f6f88fbd | -12.96218 | -48.00418 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04a21904-0486-3a8d-a920-613a7e103a75 | -14.20117 | -48.76428 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef0de23f-81f5-3f9a-932d-050eb843b059 | -12.97907 | -47.96473 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 567c8dca-bcdc-332f-b7be-1941ef32d5a2 | -14.16321 | -46.14806 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6243b4a9-8b06-3ddf-9429-06c692248960 | -10.75969 | -50.64991 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6ff8e02f-1425-305a-81be-c09c6053043e | -14.20461 | -48.76487 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25d1fb88-4069-3b7a-926b-ef56fd7755e9 | -11.992 | -46.65281 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8dca421-4ce1-3ff0-a9c1-586ee5b58c0e | -11.28147 | -50.85108 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README29.md)
