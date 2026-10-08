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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40c51fc7-14fe-35e1-9bbd-d92fe34fff61 | -3.01451 | -54.7431 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61b62f1-4b01-36a8-8fec-3ce923449568 | -2.85704 | -59.26605 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6114a3fb-9980-3a24-b05c-057e62c1646a | -3.49739 | -59.27665 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddc83011-2871-3a8c-96e8-1d4a0d18f445 | -5.08551 | -49.6971 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc54e9b7-d08a-3365-86ae-153c6ec3e058 | -2.84169 | -57.4879 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16891c59-df69-3568-9e89-72a3b79e78e9 | -6.67155 | -55.09055 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51db88b6-0cc4-3476-b5fb-8750835a2e7f | -3.51443 | -59.95155 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41518672-0c82-3bb1-a2c8-d20e2fc4d8c6 | -3.99878 | -56.27467 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef8ae04f-e2e0-3183-875f-0a4247a1603f | -2.98646 | -54.76968 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aad32d3-29c4-3ee8-9fdd-1795731a375f | -3.17974 | -53.84272 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16cf438a-20fc-392f-9607-4cb06276c41a | -2.87529 | -54.47524 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3bccd20-ae66-303f-b368-6672ca6aa5ce | -1.18517 | -55.66974 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b6094b-6f8c-32e5-b822-3249d7c54754 | -4.42575 | -59.49054 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c310ff-d492-3875-acc1-89528615d69b | -3.01132 | -54.13897 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08df0d4b-dd60-3e6a-b83b-86ca206c401a | -3.27724 | -54.05108 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5719d52b-979f-3729-acff-a55976ee7611 | -3.57756 | -54.31695 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6f729c2-2a0f-35a4-9b35-2fcbb0be8a0a | -8.38304 | -46.29178 | 2026-10-08 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb4aab7a-78ea-30eb-9764-1ca2ebfbb1dc | -3.36833 | -50.48315 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 505a1187-2ed5-3dd4-b810-ece5a3d14fc6 | -3.0552 | -53.92646 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dc0d9b4-f880-355a-9481-555b2d703d4d | -3.53628 | -59.39735 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 526bcaca-4e8e-3ce3-9e76-407e19703e0a | -3.21272 | -53.86435 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9b9cff6-af5c-3431-9e14-dc84618a7e59 | -3.97292 | -56.11381 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5c264ef-884f-3a31-bc6d-928792c5f0ff | -4.36727 | -55.64558 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98e68301-60d4-35d5-b784-89475778aaf6 | -3.59361 | -54.67911 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dce529f5-0880-35d3-923a-5bf9c1295027 | -6.27576 | -56.00202 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aede5800-6534-3bce-9784-c5d6ebcc6334 | -4.08061 | -55.3815 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b6a1f97-00eb-372e-8d48-d25f22a6a195 | -3.84543 | -55.98335 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75d0b426-0950-3c30-bae6-a63459e7f043 | -3.20446 | -50.55428 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e9f496d4-f779-32ad-a65e-548fd3874ef6 | -4.4605 | -54.89381 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa57e96c-1d48-3827-a9d7-f8b9d65e6662 | -3.29688 | -54.01797 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25241dd9-d5a9-3382-8096-ff3ffadde914 | -2.48524 | -56.13278 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a299ca56-6170-39b3-b8ab-ca6a58ddc227 | -2.82512 | -54.1073 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3f08ef2-8809-382e-a485-1cace1395989 | -3.48607 | -59.45939 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdb76cb5-03c7-3867-8ce6-1b4d37cac3d0 | -1.52274 | -54.53152 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3a5bd98-1490-3e53-a0b4-e02ee2c69ae6 | -3.95077 | -49.01091 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7c45a15-79c1-35b6-9223-07eae325b8ce | 1.09966 | -60.5143 | 2026-10-08 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cadbe726-5ba5-31ac-a71b-151ff8747847 | -4.45764 | -54.88953 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 895aa688-a9b5-357b-97d0-07dba288b0f7 | -3.26668 | -54.04937 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8efedeb-2d5e-3f5a-a811-370370903126 | -3.85156 | -55.98789 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0cb9598-8f04-3289-a8ba-d38efc73e1af | -3.01161 | -54.06774 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e035e24f-fdb2-3cca-8e3a-fa810107b7ca | -3.70896 | -59.64762 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d19eaa9-c7ed-31ba-af0f-52fdf3e2ec24 | -3.25794 | -54.03603 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fbbe96f3-36c3-3385-8602-07b6394fa8d9 | -4.15339 | -54.91577 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99565e3d-5247-35ef-9374-3184fbac21ad | -6.43358 | -60.05745 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d669105-1f27-3e16-a54e-1ade18ccc036 | -3.03941 | -54.23383 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c66ffc1-e058-37bf-a438-afb78759d330 | -5.81552 | -53.82836 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdcb9096-73f2-38d8-b223-cdc5a889bcfb | -2.9496 | -54.07019 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaef8c79-f5a6-31f4-8567-91aa746b63a2 | -6.63582 | -43.73971 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d03b4ebe-d0d2-3a0a-b93e-f9fab6664b44 | -3.59419 | -54.67537 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7977cadb-a8c9-34b4-ba26-433f3514d76d | -4.15684 | -55.13784 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b3ab3ce-76b9-3832-a538-d83ccf4602b1 | -8.61046 | -67.02211 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a804fe76-34f1-3887-86b1-e394426c321b | -4.1528 | -54.91945 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d74ff8-48f7-3533-aa7b-30a1b19cc374 | -2.34143 | -55.69472 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff18e09-1abb-3bc7-be91-416244494510 | -2.97784 | -54.05072 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4a021be-f4fc-384b-8ef2-68c3a9fea5ff | -1.52446 | -54.52056 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01bea1f6-b03a-361a-989d-5e24726675a4 | -7.60098 | -46.76373 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78b5d85c-55b2-3e56-9318-181dc9c50da2 | -8.73753 | -45.15492 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 330b756a-706e-351a-85ff-9b83e2b1eda3 | -4.15231 | -54.91879 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca46e24-7398-3428-be50-95aa387e98e7 | -2.8674 | -54.15701 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29bd2123-b646-394d-bde4-442e54e3c888 | -1.5271 | -54.81311 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3575d0-2b3d-36ce-a56e-d94314d566ab | -3.55174 | -59.49408 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ba2a29f-1e8d-3184-8598-558c8a4ff771 | -3.01803 | -54.0727 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c941f57b-763b-322c-b4ea-3405cdc34648 | -3.5726 | -59.45609 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59890d8d-1694-3e49-a727-8bc3239d6615 | -2.84673 | -57.47785 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af9f4765-08a0-3d9b-9dd5-9e0e7b582b2c | -2.9655 | -57.76576 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b189599-f155-3b82-bbb2-5310873f5f4c | -3.2826 | -54.03989 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9733cee-d4b5-35e4-a5fb-47319f25a840 | -4.38686 | -55.60854 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02789732-652d-3ba1-8ae1-9b1fa25a0903 | -1.33119 | -55.43289 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 008f2d8b-aeae-3cec-a173-e986042b8b67 | -2.15184 | -58.11389 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1674b8c-d91a-3786-a5a4-8aa4fc59dc95 | -5.68805 | -53.4874 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 141dfbe2-625a-3879-9a10-79c415c22e41 | -9.12181 | -66.01344 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1525f458-92a7-3c6c-bff7-1db082902e77 | -3.5412 | -55.52508 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 527f1f10-598e-3513-ba06-b373490b08d0 | -11.071 | -54.51177 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44e3ad00-75be-3c32-aa4b-f3f3e7025ae1 | -2.98541 | -54.77253 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 903076de-a979-3c23-bcc3-74bcb1e08e75 | -2.86737 | -54.20715 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e418fb6e-8148-3de1-9c1a-8639b413c3e2 | -3.37859 | -59.43086 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de2906a5-223f-3056-99ca-c63cf5db7370 | -6.46608 | -55.44887 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a065301e-108b-380b-8757-cb1c4df67964 | -3.1245 | -53.76244 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92b3d996-ebef-3f0e-b0ad-ade881867e31 | -3.29748 | -54.67639 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9848714f-94aa-39bd-aa86-55c6dc0cd443 | -3.05412 | -53.91014 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b470913-db47-3e03-9c8b-9c22e6e2e0b0 | -3.04094 | -53.94838 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c583180-78af-37c0-994c-45699cb7eab6 | -7.20398 | -45.35539 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f66c092d-6f84-399d-bdee-3b66a2d32e8e | -3.30066 | -54.06269 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3495faac-f49d-3245-b9e2-567e7bc8213c | -4.29494 | -54.8076 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0796e4-6b02-3b53-8143-cc32d2e7b650 | -7.20617 | -55.10584 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed51298c-bff2-3292-9504-d7acf78b6a00 | -4.15344 | -55.13726 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d252652-e9dd-3be2-9369-1c558ed7d71f | -1.14953 | -54.21958 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2723ed8b-7bb1-3d9a-b929-32f504df4212 | -6.53684 | -55.26447 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7081adc6-31f9-353a-8a62-a5b3e05795b3 | -3.02182 | -54.14056 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88843615-9eec-344e-9953-4069c4093887 | -2.4852 | -56.11152 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4240c51c-f737-3d18-b422-1e7bde1acbfe | -3.02242 | -54.13673 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0c8a550-a302-3a25-bd36-76f5bc9c1fd3 | -0.99727 | -53.74253 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e5c778-f816-3cba-bff4-911428007073 | -3.05642 | -53.91858 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80e5bee0-59b3-300b-a2db-d9ac42ac0794 | -2.76586 | -54.09108 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0bdf83c-532e-37bd-bd2f-8418ff849221 | -2.573 | -56.1747 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad73d19c-83bc-3dc9-bff9-091fdf2b792f | -1.5341 | -54.54819 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 10cf0676-7ff4-35ac-a017-b5c838fd52de | -9.08886 | -61.13818 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6493cbfd-0cab-3283-bdc3-b8293c4c3d13 | -3.27203 | -54.03825 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d45302-91d9-309f-8ac9-207b533439de | -3.09153 | -58.02492 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60b8a2cb-f592-3804-909b-f9f7068f7fbc | -2.98826 | -54.77672 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README153.md)
