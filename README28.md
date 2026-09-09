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
| fe3ba445-8028-3f97-bbb2-24f121b3be25 | -3.77693 | -58.84726 | 2026-09-09 06:05:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710fcea2-d8f4-3e39-9f59-20df816663d0 | -3.43105 | -59.26212 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| d08b3ddb-7f01-3665-867a-72ce64f781d4 | -3.37711 | -59.40952 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38d007c8-3495-32e3-aded-81f9be222cb8 | -3.95697 | -59.36401 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59a7a845-1bbb-3a5a-a318-a1dd8933c1e2 | -3.35777 | -61.28707 | 2026-09-09 06:05:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a547f340-e059-3f19-99c6-ed80dab3f8c8 | -3.77109 | -58.84976 | 2026-09-09 06:05:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4959afe3-de57-38ed-b10a-46f5e4d12c22 | -6.55362 | -62.89659 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 945e78da-88e6-361d-ac33-4841a2e743e4 | -3.96259 | -59.36169 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c56beb1-b4d7-359f-a7f3-1b738c6a1875 | -3.36974 | -59.42368 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 590996f5-aed5-3d3b-b9ca-8d52e3aa1879 | -5.18669 | -59.76127 | 2026-09-09 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1c02ea7-3aa3-3c41-aef8-ebfa968a4a38 | -3.35817 | -59.43111 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 264b5591-bfbf-338e-8b84-b016dd7cc942 | -3.37244 | -59.40572 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be03ce0a-819a-3c06-884b-0313ec41b0d8 | -6.55366 | -62.89544 | 2026-09-09 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eef45768-f0d4-3579-8e1d-4d5fdf44c25d | -5.36576 | -56.02569 | 2026-09-09 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d86fd57-fb32-3aee-aec9-616e73e1d24a | -3.89856 | -59.60693 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0872021a-3136-3a9b-90b5-803d5cabebe8 | -6.63347 | -59.44579 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c92628a-8c41-3507-943f-55992e6ae2b0 | -3.68394 | -58.52693 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7adfcf5-0a6a-3fb7-bcb3-4ab5ad289505 | -3.95741 | -59.3609 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f343bbcd-5be3-371b-b3ad-7fd979364bb0 | -7.05648 | -59.78227 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d075c45-d003-3849-9c83-126d49c2901f | -7.11791 | -56.5146 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0974c30-2ec1-3241-9599-6b09b020c884 | -7.11858 | -56.5094 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6727fb52-080d-3b25-9bda-a99b0bb86ff3 | -7.12009 | -56.50777 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36bf4347-5a70-31cb-832a-c09aefad522a | -7.06177 | -59.7829 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d76f93-f4f0-3386-8cbb-b8973ce0f11b | -6.63435 | -59.43937 | 2026-09-09 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c96d458-482b-38c0-9fca-2ec7fb589280 | -3.35728 | -59.43709 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0b817c6-d055-373f-8b1a-e3cc4c5ff578 | -3.43782 | -59.26176 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a789007b-e3be-3fe6-b44c-d2f0f8e00cc7 | -3.68445 | -58.52345 | 2026-09-09 06:05:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59fe0cf3-844c-3ad7-b9d7-52acf6cc49fe | -3.9622 | -59.35985 | 2026-09-09 06:05:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9df8f9af-88f8-3a81-a1a7-e013eaf63cc6 | -3.36418 | -59.42593 | 2026-09-09 06:05:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4de11103-a347-3167-a230-1f9b43a94add | -7.11935 | -56.51314 | 2026-09-09 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 130e51a0-d5d8-35f3-86f4-0b158eb2698a | -3.43669 | -59.2598 | 2026-09-09 06:05:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44a271c9-2f1d-3b3c-82e2-ac1fe7b17216 | -10.65656 | -58.76555 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb42223d-c31c-3405-941c-65424697cdbe | -9.34089 | -68.23415 | 2026-09-09 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8898539-faa3-3807-8e9c-ae3e8364c52f | -13.28964 | -61.78713 | 2026-09-09 06:08:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b9a6ba64-84b1-37af-9e89-b0e82f474c4d | -8.98402 | -65.39026 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e76d9fd5-bfdf-3c01-886e-99daea134371 | -10.6529 | -58.76891 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2f87f76-e170-3daa-8dd1-b9f7f660af36 | -8.98697 | -60.58773 | 2026-09-09 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee0de4b-9693-3ce6-a952-994fab20afde | -9.24491 | -65.67517 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b6a644-01e5-3ddf-bc9a-a05aed2d902f | -9.55144 | -66.3831 | 2026-09-09 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24216966-30a8-30cb-af09-25b3a8195217 | -10.64996 | -58.76992 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40dfe5d7-8c48-3855-b772-085608463f9c | -8.98265 | -65.39226 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa822f7c-d8d5-3d0a-9b71-392b39e724e3 | -8.98639 | -65.39281 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f12f63ed-3b08-3291-9bbe-96c1ebd519f2 | -9.52691 | -68.274 | 2026-09-09 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5eb6ef1a-fef3-3179-a3f0-5250f301abb0 | -9.01876 | -65.41383 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aace8e6f-a813-3724-82fd-428ebbee0fb9 | -9.24925 | -65.67139 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa0e6c68-8b4a-3d29-a361-991a956e6b67 | -9.75335 | -66.6188 | 2026-09-09 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d58ef34-daa9-3fc7-8560-3879f0f52c93 | -9.52129 | -68.63969 | 2026-09-09 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfd526d-19c5-3700-a0d0-59ea2906d941 | -8.98674 | -65.41571 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8e3dddf-4590-3616-ab9c-df6c19037b12 | -8.98739 | -60.5847 | 2026-09-09 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 812b8133-2cb7-374d-aaab-acd6a90ae3c7 | -9.14579 | -67.82554 | 2026-09-09 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebd4bdf6-8ae6-3de5-b81d-01ae3dff900b | -10.65059 | -58.76506 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8f3f3b-3b6e-3aac-8486-70aa88476e03 | -9.23683 | -65.75385 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb85f87-b451-39d4-82e9-3afe3bb0789d | -8.98824 | -65.41377 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87655358-aa03-364e-9e9c-3c671e7be843 | -9.03922 | -68.50581 | 2026-09-09 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862b39c8-6f34-3123-9ab2-2c9054765fbc | -8.92469 | -66.85889 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71f51b09-ad1c-3f67-87b3-37da0e55de54 | -9.32463 | -68.20602 | 2026-09-09 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18ed7e9b-ed9d-3061-aef9-4654058bf119 | -10.65598 | -58.77005 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04ec7426-3a82-3a42-b1bb-61f6ec4ebda2 | -8.98776 | -65.39081 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a57a4a2a-a924-343d-ab2c-c21e614f54c6 | -13.29038 | -61.78126 | 2026-09-09 06:08:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 95a0e3d2-05a0-35df-a437-abc580c7278c | -9.48688 | -68.34467 | 2026-09-09 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fa06bdf-8436-3c2d-9076-5d364d4d6722 | -8.92121 | -66.85836 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc6a4c39-602d-3b0f-8d9b-b9d15dfc510c | -8.99197 | -65.41434 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcb7c49a-75e4-366d-82a7-2b26db47fc10 | -9.14636 | -67.82192 | 2026-09-09 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e5d5570-1014-3066-b57a-48148c73f8e0 | -8.9878 | -60.58169 | 2026-09-09 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a0f1cc3-f918-3251-8382-c320b2bd31a9 | -9.47794 | -68.33598 | 2026-09-09 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc727727-d414-3b6f-9ac9-a041a56b44c2 | -9.2486 | -65.67572 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1cd07b-4249-3019-93b5-8f391be6427f | -10.61956 | -67.92822 | 2026-09-09 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cab5b2dd-64e5-366b-a932-fb6d73e82ae4 | -8.84018 | -67.03042 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30ca5aef-b5e7-322b-926a-013c1d747ef6 | -9.01437 | -65.41774 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e653f206-04b5-3dc5-a650-6bcb5d9d2f15 | -8.74924 | -72.77041 | 2026-09-09 06:08:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ef967c-1744-3931-916e-39eb155e2101 | -13.28387 | -61.79233 | 2026-09-09 06:08:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98ba8a1f-9c63-3bbd-810a-2b2119f37742 | -9.00625 | -65.42106 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08dafc2-70d4-3a6d-b68c-00319616826b | -9.24556 | -65.67085 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 436c26b1-418c-32f5-9821-19f5d77aea9f | -10.65888 | -58.76926 | 2026-09-09 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8db13ad6-7329-38ba-931c-34451cfa9030 | -9.00998 | -65.42164 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1183036-02ed-3088-acf1-7e3457d14c0b | -9.01064 | -65.41718 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 972ccb71-a987-3914-a445-05e3c9222012 | -8.98333 | -65.38779 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae6ad6c4-4886-3e46-8930-d11dbf85e670 | -9.01371 | -65.42221 | 2026-09-09 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b2c55bf-ee7b-36c2-8b09-0fb8f33f579e | -9.01265 | -65.4262 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05ce834f-8cea-36c3-9593-6ab14b7a1a09 | -9.01318 | -65.42226 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 007000f6-83d2-32d5-8bef-3b030a9ae491 | -6.55501 | -62.89837 | 2026-09-09 06:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd7c8474-b5dc-35f9-948b-9fcda873e9f1 | -9.01371 | -65.41831 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084fb8fa-2a9c-302f-b833-f9bd42f4e757 | -9.2471 | -65.67545 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 574102bd-8823-34f8-af9d-498fded037d8 | -3.15083 | -60.65662 | 2026-09-09 06:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 640d6274-be1e-3784-9708-d440f0d71a13 | -6.56225 | -62.89375 | 2026-09-09 06:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 191f11cf-fcb4-360a-95af-b9283d481a5a | -9.00924 | -65.42036 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e12fa7f-b959-36ac-bf23-1af5dbbeacbf | -9.01445 | -65.42511 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c92a644-63f4-3f07-97c8-ddbdbe4cb67a | -8.51528 | -69.79671 | 2026-09-09 06:27:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f01e407-357b-3d84-a748-a4d92f32f019 | -9.00747 | -65.42144 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb8afb8-d635-3a62-a041-beb98f54a487 | -9.24145 | -65.67483 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c68c3456-46a3-3238-ad1d-c332073fc400 | -9.00694 | -65.42538 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660115de-df7a-3b7c-b9ae-76b176522241 | -9.00874 | -65.4243 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45caeeb3-6982-3c37-8f16-0d70c3e5dd88 | -9.01546 | -65.41721 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e368f354-3ad6-3e65-9305-eff28148d9ee | -9.008 | -65.4175 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a40c92-7af0-3e49-9ba0-64aa2fb8a7b6 | -3.15789 | -60.65779 | 2026-09-09 06:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e588e0fe-d0a6-36ec-a467-ed2f4c126d03 | -8.51049 | -69.80001 | 2026-09-09 06:27:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bec4277-d623-3440-b83c-9133c378e2df | -9.01495 | -65.42117 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b86c8f-7e5b-3c63-888e-ae9bcbd00493 | -6.5615 | -62.89926 | 2026-09-09 06:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 789560a5-7493-3ab5-a337-e9954936e15f | -9.00974 | -65.41641 | 2026-09-09 06:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dbbbca1-ca6b-36c9-925d-bab5e2434285 | -9.52002 | -68.64017 | 2026-09-09 06:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
