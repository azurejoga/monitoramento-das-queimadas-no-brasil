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
| 4096f9ab-3a11-3821-bf45-a8c2cfbc7fd0 | -10.7898 | -47.70984 | 2026-08-05 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0e1978-ba8f-3bd7-8fe5-31a4eb6117fd | -11.18029 | -54.87179 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea66769c-f8d3-3861-bccd-53362585cc5b | -11.17427 | -54.86873 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81e292e7-f402-3fa5-a8f3-531325dae643 | -6.56824 | -56.52232 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65877689-daca-3ed0-b539-53a427b7f938 | -9.28315 | -60.6515 | 2026-08-05 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c67ce32-7a33-34b4-ad35-f9d9d87cec2d | -10.45865 | -50.2327 | 2026-08-05 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b3b280b-1ac7-3e94-9b28-1cdc2500b01b | -11.17255 | -54.89815 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 526aacca-d406-3a4d-839d-3bcbf222e070 | -11.18002 | -54.89924 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb66c2ed-0f70-37c3-a1a1-5d2103fabe2c | -8.3545 | -45.97932 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 925f6033-edd7-368a-9591-cc1574244b8f | -11.16335 | -54.88308 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f82ff7-d376-3e52-af6d-a683da909571 | -14.16086 | -54.40213 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c205a390-1751-3da2-af48-e3576e77c66f | -6.56775 | -55.15639 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e05c17-c3e8-34e7-8038-6d6da71fe83e | -11.18216 | -54.92027 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 288b640d-3ec0-38ce-9f5e-3ecdda3608eb | -10.88519 | -50.15203 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea4e2da2-c037-35d9-9c11-b9d98d750905 | -9.16851 | -56.93542 | 2026-08-05 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e2f727-1867-3882-8230-ac0dfcacc15e | -11.18845 | -54.90296 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a36e3a0d-de50-3c37-beb2-6bcf9a3f879e | -14.19573 | -54.42412 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed333d44-0ccf-354d-9edd-b8746b0f0edc | -11.20304 | -54.85448 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d522bfd4-a4b1-3c36-86e2-5e0765a30b88 | -11.1779 | -54.89682 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 106a0983-7c08-3ed1-b42c-851a8f7d7086 | -6.55496 | -55.14641 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13a7871b-210c-375a-9367-44bcb7b6ab46 | -11.21896 | -54.90281 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93ccff69-3261-3c65-915d-23f16fb55136 | -6.72137 | -58.92761 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ae7c941-8c3e-3a3b-ba9b-f971e3b6451f | -6.01062 | -47.4024 | 2026-08-05 05:23:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16531429-c29f-3582-8620-184f54ecc3d5 | -17.9803 | -47.15581 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f9161e9-712c-3795-bff4-609a437214bc | -11.18548 | -54.87037 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98e9832f-fe93-30e4-bf04-e4877f6ad90a | -6.96209 | -52.81572 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 571ba502-b2fc-37cd-8c00-d894ed1b543d | -17.98632 | -47.16414 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| add67c37-ae7b-382c-a2d2-7e164a8cba37 | -11.17321 | -54.8937 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 399d333f-e76c-3c7d-a274-c7479efb24b7 | -11.17655 | -54.87124 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fecb1afd-4c75-30c6-87a4-0583769426e5 | -11.19426 | -54.86238 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 557e870b-5784-3257-be67-552f14055e91 | -10.91627 | -50.42266 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63135492-988d-329d-9ead-6a4113c2f9b2 | -6.53278 | -55.15089 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 966d8a5f-8935-30cb-ab47-b1aded5087fd | -11.17162 | -54.9141 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dc71ebc2-9c7b-396e-b1a5-52511d3aa75c | -5.25046 | -56.96017 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a779ddaf-12da-39ad-8078-13b95bc137f0 | -11.1069 | -50.40311 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e967d4e9-eaeb-3981-9e58-d4e53d184602 | -9.28443 | -60.64368 | 2026-08-05 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f44fa6fd-45dd-31ae-850b-ccfe34148321 | -6.55138 | -55.16968 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bda815f-8eda-3fa3-9eef-954d160daf48 | -8.33996 | -45.98169 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e4b8bed-ac75-306c-a976-b38947a052b1 | -17.98695 | -47.15716 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a04937a6-5da2-3581-af39-e588dc52c37c | -8.35351 | -45.97839 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1ec15a95-da2e-37d0-8aa8-3ebbc6633561 | -6.57105 | -56.54817 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62787bb3-23d5-32e8-a2c5-68513ef6f3ca | -11.18729 | -54.88446 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c97e44-1108-34b0-911a-18862023275f | -4.05596 | -56.22787 | 2026-08-05 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b6dd4f7-f918-3b04-bee0-6d77a865ca20 | -6.55018 | -55.17746 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc1e34ab-a672-3386-89ef-bf9031145b27 | -11.18068 | -54.89477 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 267dc79a-f092-3ab8-953e-f261f47bc25a | -9.60673 | -47.76894 | 2026-08-05 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06ff4732-5caa-33dc-9c89-4c0018866232 | -4.91755 | -62.31972 | 2026-08-05 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64e7824d-4ad7-3538-9d0a-deb968a97dc2 | -11.17801 | -54.86929 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52859a59-458f-37d6-ba3a-2edd57b33b5f | -11.18652 | -54.91637 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a31cdfc0-9be1-372d-be38-e05ea17a5c5f | -11.19721 | -54.89505 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 778b47d6-288d-3adf-aa03-2ded9d5bb387 | -11.19089 | -54.91245 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27675163-c2fc-3f54-997e-88bbaec70bbb | -11.20467 | -54.89619 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6071b2bd-30d4-3f3a-8fdf-a17c8a723f26 | -7.63126 | -45.31104 | 2026-08-05 05:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83fc27a7-c52f-3359-894f-d9b0221a5758 | -11.22418 | -54.86687 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5991bf56-2e1b-3be2-9467-7066bc0fc493 | -6.55197 | -55.16583 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c694f3-12ba-3a18-883c-8c28e87d0e63 | -6.33895 | -55.73318 | 2026-08-05 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c981546-fb8c-3dc8-89e6-866393a67c19 | -11.20581 | -54.91468 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbb8e610-e70a-3113-ba34-1b6abb874ee5 | -11.21766 | -54.91182 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4672ea27-ceb0-3405-8e0e-44527ca8e609 | -10.45941 | -50.22687 | 2026-08-05 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc90e1a1-26c7-3dc1-a31d-d6c128960713 | -11.18589 | -54.92082 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3402733d-8996-3da1-8ea5-fa4da769102f | -11.16312 | -54.91035 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5892f98a-5fbe-3d0c-be85-1a7eac6a36c5 | -11.18961 | -54.92137 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a909c1-a088-3584-9053-e95f920eb6aa | -11.16641 | -54.88815 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2685f049-7713-37c5-b82f-095c55c5933d | -11.22108 | -54.86185 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d442f81-f8d2-3478-82f8-ed4e0baec5d3 | -11.17853 | -54.89235 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 032a2d10-5c04-3d25-bee3-045884e1d686 | -6.58556 | -56.54322 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9abbc90-edec-3ca8-a54c-5edfd9ff77a9 | -11.17057 | -54.91148 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5bcb17e7-9de1-39b8-a478-590d4fc08386 | -10.60937 | -46.37585 | 2026-08-05 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fedef2f-6d1b-3070-8c4c-a4a122cbe1b2 | -14.17787 | -54.40577 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8b95144-8076-3e12-b799-cdd9330dfcc5 | -6.72079 | -58.93121 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c45647-cec5-3df1-abc0-fb7b002334cf | -6.95735 | -52.82024 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3d3e5d-a5ba-32f8-b185-3d33b72ab962 | -11.17588 | -54.87577 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7188e46-2705-3e65-9920-0c442d824869 | -6.56835 | -55.15252 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6397fe7b-c960-38fc-bc13-26cfcaf818d0 | -6.54669 | -55.17692 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 432912f6-97e2-3abb-947c-d51b2eaa1261 | -11.17868 | -54.90818 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8e7df4c-8a27-36bc-a7b4-53bd120ff492 | -6.55436 | -55.1503 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e14a7694-2ba4-34f7-b8d3-040e7f4b237f | -6.71905 | -58.942 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2040a972-8c58-3694-8777-67e9b5ac2640 | -11.17726 | -54.90129 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09907ecd-d950-33c5-a420-c96a11959d13 | -6.52929 | -55.15034 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d21d6ad-5b55-3d6e-ade0-cd759188a9dd | -6.57125 | -55.15693 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517269ed-cb09-3867-862a-6a98b91cd5e5 | -11.17349 | -54.86613 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d78712-f7cc-3083-bfc2-738a4ea112a0 | -6.7151 | -58.94505 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88ffca31-c0da-325c-a629-5cb5cfbbc770 | -14.19425 | -54.43489 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33d240ce-2daa-3228-9351-745b4f26b45e | -11.2094 | -54.8368 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0504bf3-94da-30fe-8042-13eb996d44e1 | -11.21214 | -54.89724 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9568d5b4-7992-332f-9964-6083d0b50fec | -6.57184 | -55.15306 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 076bdcab-1552-3a8e-be14-e31325bdea79 | -11.16402 | -54.87857 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d12fcd9-0682-335d-8bc8-b6c67ec9f56c | -8.34068 | -45.97627 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79f279ee-9d57-3224-ab86-956fed022175 | -11.18472 | -54.90241 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04ad3db7-63fa-34d1-b8e1-fa02e198b91c | -11.19398 | -54.91745 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d8501ba-6807-3594-aa53-2fb2c0bda0cc | -6.54967 | -55.15755 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 770b8b6d-2fc3-37d5-9a23-c134636a921b | -8.34741 | -45.9836 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e2502754-5764-31aa-800a-2a8c4a23815d | -11.18419 | -54.87943 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e1ce356-c22a-368a-b18d-321287f81299 | -11.18407 | -54.90689 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ea676dd-6c29-3f11-a287-684660824bdc | -11.17802 | -54.91264 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56e43bee-6a85-32fe-b2b3-b966f19d7e1e | -6.56886 | -55.1724 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9775f0b-295b-3fb5-b924-1cb8da334fc8 | -15.00731 | -59.44258 | 2026-08-05 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19c47bac-0c5c-3999-8a8e-54ab6b66bbf4 | -8.34638 | -45.98271 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e0f71d9e-eb2b-3fb6-a2a4-2d0062ffc120 | -9.14757 | -49.66576 | 2026-08-05 05:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91e71a64-10b4-39a4-b321-f8a71d635d13 | -11.18151 | -54.92477 | 2026-08-05 05:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
