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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9a530ba-a239-3198-b4f6-0652827d38f7 | -5.87493 | -53.63188 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1e861f5-ed5a-33ed-8540-7cf72c0be74b | -9.20814 | -59.46419 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 581ff4d8-05be-3af4-8a29-ecba0bc70f6a | -9.22804 | -59.77492 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfa20701-12db-3e4d-b8a7-09e8d4163c64 | -5.45 | -60.17406 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fff28a4-ab50-3838-9a99-3aa711556762 | -8.86706 | -62.40316 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e0a92ac-da21-3179-9621-6309cb1d1b70 | -9.09485 | -61.42893 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8619d30-f5e8-3ceb-abca-8cbe03a1ff65 | -8.6042 | -62.61443 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5763849-2e1f-33df-8548-ef2713e9f516 | -7.58578 | -63.44147 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 475597df-06fb-3670-8238-cf2c6637851f | -5.80728 | -59.2184 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b65ab24-5de7-3f7f-b58b-286c8a18d732 | -11.74076 | -58.31726 | 2025-08-22 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c780220a-55ea-3285-ab97-dfc6b68f9609 | -9.51496 | -60.55051 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e674d2b-8fd8-35ae-9179-d3e86c06a7c3 | -10.45994 | -59.13652 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02caebfb-4857-3d70-81e1-9aca58d2e0ce | -10.86274 | -50.83405 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 12089d18-a394-325a-85dd-cf51b2e4f192 | -8.658 | -70.03816 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edfe37da-e9cd-35e0-bb3b-2b0e84fdf60f | -8.66728 | -70.03555 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc7ff2ec-3ae4-3b42-b3f7-c055ecaf6a75 | -9.10258 | -61.42595 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2268a724-332a-383d-ab81-6973daf82245 | -10.11098 | -57.76301 | 2025-08-22 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61dceb62-af13-3e6b-a165-816e8c33bc2b | -9.34452 | -62.58444 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8d9e0d9-5527-39ae-8884-b4aa94b4a194 | -10.10951 | -57.76066 | 2025-08-22 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fbc24fe-e58e-3496-abdd-1183431b35da | -8.7157 | -69.46085 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7788177d-6e38-3af5-9eaa-c8862d670d2b | -9.21609 | -59.46532 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd6faef7-4455-3499-95cc-f8d7586715a7 | -9.20206 | -59.46171 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12099e2d-0de1-3733-ae08-bffae0c06bd7 | -9.20852 | -60.79381 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 058e5bb2-4256-3fb4-abce-d9ff8d6608b2 | -5.80142 | -59.21926 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8af19fa0-86e2-30ff-9b6a-24a91badfa9b | -7.56155 | -63.85498 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4723d8ea-45f9-3cf0-bc3a-3dfcc03a70a4 | -9.2122 | -60.79435 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0211bf8-4f1f-3604-a63c-6fb25d9ec473 | -9.5052 | -60.51231 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed32b21f-f65b-36d7-a4ff-da07fb85d152 | -9.175 | -59.69973 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a78c33fb-ba22-342e-822f-bfb91730cd9e | -9.88275 | -60.29331 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21a20a7d-dafd-3b8a-9fd7-96916520b112 | -4.10188 | -60.65995 | 2025-08-22 05:38:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4e97bf2-28fe-30d6-8b3f-db82d6e21da5 | -9.5083 | -60.51738 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bea28023-75b6-36f1-b9a5-b61c95156586 | -9.93332 | -65.00599 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4403dac4-24bb-3ad9-8a16-e2e86df33071 | -5.88462 | -53.62429 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2754957-3398-3fe2-8771-c764aeb30956 | -8.37608 | -70.25964 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0201c72-86e7-30a5-9b85-3af726f29b16 | -7.72004 | -66.9186 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6b7623c-7005-3bf6-822e-b92813a549e9 | -7.58632 | -63.43798 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72d9d3c0-110e-3cd6-8b23-11bc7ea4772c | -9.20788 | -60.79814 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02a72d76-5fbb-3870-bb91-50709a0e8769 | -9.52308 | -60.54715 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 095ef065-0b3d-3e5d-80d5-a61009505219 | -8.87103 | -62.4227 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc8cf4b5-1eaf-3434-906a-b8d3634e37d3 | -5.44125 | -60.17869 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 323f34cf-98af-3f3a-bfef-a1fed20dc152 | -9.81961 | -64.27195 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab957d3a-ca04-3417-9b76-540d6c892d33 | -8.54726 | -66.95377 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b855afae-4625-303f-9c7e-e2016a0f5f2e | -5.87387 | -53.61909 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc34261-26cc-3cad-8034-e7b30757d2f2 | -6.44871 | -53.37912 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70a673bd-50b6-3cea-8131-984e5459299c | -8.61211 | -62.60821 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61fb59be-b442-3bdd-95b4-9de646263362 | -10.86356 | -50.8271 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0880575d-f871-369d-b4a0-ae58caf25a5b | -8.87445 | -62.42323 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18042277-e689-32eb-b1a1-d2d9df5ac78c | -8.8682 | -62.39578 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22a16b72-a388-34b3-ac20-976d2997d3d2 | -9.66809 | -67.24665 | 2025-08-22 05:38:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a65d0f4-ecd5-33d3-8291-0f70284cc3ff | -6.26572 | -53.67569 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d7198ed-9614-3bad-9925-188b635c623c | -8.83922 | -69.11023 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10dc6791-d7b6-3428-864d-9380a9310145 | -9.82293 | -64.27248 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ff5e89a-431d-3cec-97ef-7902dd547376 | -4.608 | -55.75326 | 2025-08-22 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70c1d40d-d99b-3356-a75b-e20649acea57 | -9.22948 | -59.76506 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62412661-667e-37e9-810d-95434dbcb5bb | -9.22558 | -59.76448 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e524db3-e81d-35be-84e4-d198143ee1f8 | -5.44981 | -60.17141 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a86f902-2bab-319c-9c68-c3e278bf5fff | -7.77684 | -66.96046 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b336a7da-12f5-323a-b841-5354d90d850d | -9.51513 | -60.52299 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8799f906-01d0-3359-85e5-3918cbcb9315 | -9.10197 | -61.43 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72f44fd7-90f5-3665-9312-652c2c93366d | -8.67325 | -69.72663 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8317137d-363c-3b61-bee1-c7bd4281f2d5 | -6.87303 | -59.82435 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 155ceace-11f0-324c-b788-f1c3dfcde341 | -7.71937 | -66.92274 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ef7998e-ef7a-315d-a278-f3143fc97dbe | -9.22415 | -59.77435 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5628b076-5087-3944-906f-55b2b24a767b | -9.18607 | -59.62494 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29f8d32b-c996-3d00-a2c6-249c849de5cb | -8.85852 | -62.4132 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7e2748-4821-3ea3-ae0f-5a863e86b06e | -7.55768 | -63.85793 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf522ab-8c42-322b-833e-04f4fdd4533b | -9.17036 | -59.70416 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7ed1071-ad73-3360-a8b0-73bbee1195d0 | -7.72724 | -66.9198 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da64ca52-73b1-31ac-b42a-74401cd69f20 | -6.44181 | -53.38637 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 700e7f17-52e6-36f0-ad31-d3bbc9fc7b08 | -7.58965 | -63.4385 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8822a350-5c55-371f-9eb4-38c5c1e3d3e0 | -8.66229 | -70.03887 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab13d9e6-80c1-3461-9a69-42672cec5da4 | -7.09015 | -63.08423 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1983765c-96b1-3b22-9f0a-7766c19cc653 | -9.65523 | -63.48563 | 2025-08-22 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb0f65c0-e429-3f9a-9607-a2764f7929ce | -6.57161 | -59.87714 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4f6b65-c7f8-3993-812c-d0a7c0093ea4 | -9.91268 | -62.14533 | 2025-08-22 05:38:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd496b39-dabe-354e-a2d1-b8ff58196ad8 | -10.86986 | -50.83493 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80852cf0-7c5f-327e-9519-5d29990c6cce | -9.17872 | -59.59307 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6628889-8757-35bc-9a19-58c132cc4946 | -6.8971 | -59.89475 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8abedc5-93de-3482-9b01-9025322b9332 | -5.80911 | -59.22041 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c96bea4-096d-345d-a7f0-3c0474640c9e | -8.86478 | -62.39525 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46cccf16-1e2c-3877-8992-69c66a7b7ed0 | -9.75245 | -62.76683 | 2025-08-22 05:38:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dbc7a4a9-c676-39f3-bcc4-7d1008ef3a5d | -5.22085 | -60.28675 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d244434-217d-3b4f-9abb-745aa6420076 | -8.88128 | -62.42428 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31ca729-b6f4-34ae-8f62-15018b982329 | -9.0978 | -61.43351 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf356f8e-2326-3518-a3f0-e81a9da2af9a | -8.67499 | -62.87705 | 2025-08-22 05:38:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4efe23e2-58ad-31c8-b277-90545a4b2db3 | -9.21398 | -59.46341 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 515fba10-3fde-31ec-af20-0193613f0933 | -7.77752 | -66.9563 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a67bcd97-d031-3685-a265-20c724017463 | -9.52439 | -60.53816 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8cbcf97-51b3-35da-99bb-b22e5d17fed7 | -6.44206 | -53.39275 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2183c1d8-364c-3c76-b13f-d3d61fd4b537 | -8.86933 | -62.41108 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17519113-b273-3897-8b98-63a802753136 | -5.80798 | -59.21366 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08841edb-84eb-3c8d-be7a-75128dd419f6 | -9.19248 | -59.63282 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc01f6d3-ea51-39ae-8e7c-8328da80108a | -9.20131 | -59.46683 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b9f1f94-a665-3d4d-aaa4-1f544dae2878 | -8.61381 | -62.61965 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7391119-7d9b-39a5-ae31-8f964a890dc9 | -4.82958 | -55.76982 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16fc6e7d-5cf6-33e1-b9c2-1b5ee1cd759f | -10.10648 | -57.76232 | 2025-08-22 05:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b603b1a7-56e4-381a-a3ef-90178754d664 | -9.88656 | -60.29388 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de4ed869-91d9-39dc-9635-c46519b64bf0 | -7.71576 | -66.92214 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54da4716-7f25-37b3-971d-81d5954d6c66 | -9.18926 | -59.63054 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec9ee75d-460b-3f3a-8caf-de01da1d70d3 | -9.20686 | -60.9295 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
