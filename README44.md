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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb5a003f-5fb0-37f6-b2a6-272bb3c85251 | -8.20257 | -61.20228 | 2025-09-21 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84927264-704f-3376-b681-b4b28234077a | -10.25051 | -68.825 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb81e022-7f65-30a2-ba53-59ad26b17e7e | -9.44711 | -56.71296 | 2025-09-21 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 702cf921-e2fc-3448-9960-9c7e50dd4199 | -10.67187 | -68.87239 | 2025-09-21 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b38e3baa-5ef1-3d6b-a5ab-249178410dc6 | -8.98524 | -65.45311 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 419c4a31-2ea3-382f-992d-f7ebfccd391d | -8.19951 | -70.99218 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c22332ba-257e-3283-a282-6b5c7e6ef5d1 | -9.17996 | -67.76247 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e50f1f3-4f07-306e-b04a-1efc2ef57400 | -10.09562 | -68.51446 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c3547ef-202d-3ede-8151-d833d3847d4d | -10.89535 | -68.21358 | 2025-09-21 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1139258a-da5b-3644-ab6c-dfb8582ae998 | -8.86418 | -67.10338 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4998fb33-1c07-30b1-b6f9-5824147b180d | -8.53559 | -67.07274 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1e890dd-7ec1-37af-a99a-f10304a1ce81 | -10.61936 | -69.47887 | 2025-09-21 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41b56b90-55e2-3f45-a97f-1e33691a8e6d | -9.48567 | -68.83939 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bec6686-9958-3424-b7f9-34225f4ea21c | -8.78724 | -68.84009 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 429c5024-1ae2-3980-9d57-f3ca999ac0a2 | -8.53452 | -67.07968 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c2201f8-eca7-3f4b-87af-400b6350bb4d | -9.33078 | -65.32018 | 2025-09-21 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f81907-4a7c-30e7-8cc8-18c413fe4bdb | -9.1189 | -66.01314 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4948b5a9-7ede-3676-a2ed-bebf0c9ecdef | -10.66604 | -69.10139 | 2025-09-21 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7bfaeda-e9f8-3f4c-b252-9deb123a47a6 | -8.98924 | -65.44986 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d299813-0ae7-3a84-b49d-737628b18925 | -8.84423 | -68.97833 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 320f71c1-2f50-372c-94c3-479c835b18cf | -10.17121 | -68.16445 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17fda85f-c82f-330a-a88d-78c85e48ad54 | -10.09544 | -68.83633 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d632255-1693-3b87-926d-fb24ea969c37 | -8.66814 | -66.58857 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4fce294-1735-378c-a3f6-0cb4d29e2f14 | -10.16228 | -64.73586 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f05ff57-9682-340a-8492-84ddd5e92955 | -9.42778 | -67.19635 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f27c69c-f994-3ec3-ac43-ef62fd265c6c | -10.66547 | -69.10498 | 2025-09-21 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42bf6cd9-32c3-34ed-86fe-188de27b6feb | -8.71081 | -69.10959 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f01978d-5c07-3032-b128-0195c4bc9b68 | -8.57337 | -70.88862 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7076f1e3-fcb0-3d94-ae00-2bed27f499ab | -8.7924 | -69.0219 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a07f55b-83f4-3114-a6d8-1c4388a1e091 | -9.02069 | -65.40418 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db075d56-83e2-3cc4-9b84-6d998b96e7ee | -8.26708 | -70.83285 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 923b143e-7288-3e0b-9183-f98659ecf3ee | -9.41306 | -63.69996 | 2025-09-21 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a4b4f80-9712-3f3a-98d2-afa734a688ea | -9.46124 | -68.94913 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 894623ce-7893-3bb1-b278-3db3e6a5780c | -8.85146 | -69.1805 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05ee0ff9-69f7-3c30-a965-88db96a6feb2 | -9.74072 | -68.43526 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d42ded-b3bd-3520-a547-e51e257c542c | -10.28433 | -68.82681 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27a78715-cbbf-341c-8fc7-9ff186be6fa7 | -8.53836 | -67.07672 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec884ceb-b6b2-3fb4-a23f-7d0f3e48fe1f | -9.31502 | -68.82255 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 322fc46d-2820-3180-b653-e5d2a76e759c | -8.84891 | -71.35306 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 480ea1e8-fbb3-376a-9271-baeeef158274 | -8.63384 | -63.28469 | 2025-09-21 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03cc5e26-7b85-33e2-8557-8646c4ab8ca4 | -8.72514 | -69.17178 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d72da4e-7547-3acb-b69a-b57af96d753a | -8.7792 | -68.97531 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d050ab9-8376-331a-a86d-e74f83888c13 | -9.33426 | -65.32064 | 2025-09-21 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af58d715-5470-33d1-9178-71f0754d7f68 | -8.2235 | -71.02591 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec0f72b5-4c77-3473-862c-dda4db16ecbe | -8.50965 | -67.01879 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d7b7ce-12ef-3d1f-9611-2ab686576f69 | -9.37997 | -65.83757 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8eac13-6ad8-3093-9847-a873451601b1 | -8.51019 | -67.01532 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08639a36-445b-3b45-9f7f-083b7b7bc5e5 | -9.44988 | -56.71383 | 2025-09-21 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a1a97e8-017f-3608-a653-c96cd19e3993 | -9.96859 | -68.80074 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5413d9-9561-3ff6-8a7d-8212dba79f38 | -9.31863 | -65.89312 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0fa5d77-843b-3493-8448-4aaa539a54a3 | -9.4093 | -63.69938 | 2025-09-21 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1a77e6b-27e4-3545-9a0a-ee704a29236d | -10.69362 | -69.71677 | 2025-09-21 05:50:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f18b453-bd5f-3937-b38d-1f2d04880729 | -8.49509 | -70.61708 | 2025-09-21 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 825313a7-c54b-3eaa-8e50-dc67baa4bc45 | -10.0543 | -68.45387 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e8e501c-ad96-31d6-a917-bde76e381ef9 | -10.10687 | -64.88789 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2813d585-3f73-3ba1-8e2c-219c7221888f | -8.57209 | -67.83896 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ec59bd0-8c7e-30af-976d-2e53a122e05f | -8.49359 | -70.6139 | 2025-09-21 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057fea68-cadb-3ca9-9872-3fb9cf538386 | -9.59397 | -68.71475 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4913a689-5a84-3182-babf-5cc28f8af14b | -8.87725 | -66.81946 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b87253-5db3-3070-bcad-8c0084745b76 | -9.74016 | -68.43876 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26452f54-a9f1-3cab-812a-44493ba16665 | -8.22717 | -71.02654 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5549c89-bbbb-395f-b48a-f48203779158 | -10.15808 | -64.73949 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b74d866-f86a-3e08-9322-ed06def28f96 | -9.09054 | -68.47787 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd95cd5c-d516-3305-a6e1-2be8cfcc789a | -8.00519 | -70.3088 | 2025-09-21 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 312dfb6b-0619-329e-858e-1a1db9f688c2 | -8.28245 | -70.85294 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af293398-84a5-3bb7-b2a6-19240361ca65 | -7.98369 | -71.33992 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04385713-039a-3dc7-8cec-ce52a7bb0e3a | -9.74348 | -68.43929 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88e8676-322b-34a1-b3d0-00358bf5c3df | -9.47231 | -67.89075 | 2025-09-21 05:50:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c455b379-d5da-348c-9b27-825767546e33 | -8.53121 | -67.07916 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30fd09ae-8d76-31c9-a273-c102a897b635 | -8.20315 | -61.19806 | 2025-09-21 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e860f15-705e-3d43-a7c4-0e6c06d7e716 | -9.44932 | -56.71839 | 2025-09-21 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8effa516-a5bc-3587-bbaa-e78f1147aa09 | -8.20199 | -61.2065 | 2025-09-21 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612a976e-c580-3056-bc06-74286abf303c | -15.81606 | -59.51773 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dc108650-ae63-3ca0-9c66-df7cbc98b080 | -15.81522 | -59.50883 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8fdaabf3-0ec5-3c28-9658-fc0177570b81 | -15.89515 | -59.40189 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e98bad8-c1b2-3a3c-8bb1-541175a3d4d4 | -15.77131 | -59.45885 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 227d62c1-b9c7-36a1-bcdd-25b92ad04207 | -15.93093 | -59.44084 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19862374-9ba1-3a45-a87f-7b5435bab9d2 | -20.54049 | -56.14372 | 2025-09-21 05:53:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77ab6300-8c3f-3b54-9328-ff567688100e | -15.95957 | -59.43202 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21b07885-edfe-3e3e-87ff-620217b5ac45 | -15.8164 | -59.49869 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a5a113e-4793-33a9-9f2d-017fda0387c4 | -15.77636 | -59.46296 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0eb0e695-a45b-3f34-8e4f-4ef3797f45b5 | -15.96689 | -59.41579 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a491fa3d-931b-3bcc-a3bd-d598b1f35cb7 | -15.82753 | -59.51352 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1458ac1d-f4c7-38eb-be54-96e9070eea55 | -15.97267 | -59.41377 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6550a77a-feca-3704-8cfa-17fd44b7f8c8 | -15.95453 | -59.42737 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf6456cc-37c2-3f2d-9147-81e51df60f2d | -15.81864 | -59.49397 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70d8a00a-071c-37ba-b18a-27f8ae6de7c3 | -15.81785 | -59.50127 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23aeee28-c6f9-3b69-a9a4-a34adb74c16f | -15.89598 | -59.39445 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dcfb308-6a38-3dcc-ada5-6811766d705e | -15.77421 | -59.43288 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af486f24-e3ad-3d2a-8dfc-fa44be844346 | -15.97122 | -59.42686 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cfc3ed6a-2794-3000-9292-d913cfa94982 | -15.97309 | -59.40994 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 62c4a3d3-d50b-37e9-914d-494ec6996500 | -15.96617 | -59.42234 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 93c2429f-1797-3c4e-bd51-51fa3424540a | -15.93221 | -59.42888 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2df998ee-89cf-3cfe-882d-5a1a22754163 | -15.93178 | -59.43285 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edd2e890-8063-343d-b21e-c13ee4c8b6a8 | -20.54204 | -56.14626 | 2025-09-21 05:53:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d701149f-be55-3828-80c4-f5487a7a7537 | -15.8272 | -59.51649 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f07fc1bd-2e6f-38a8-96ab-2e51bd17e84e | -15.97192 | -59.42055 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c5b763b1-9531-3b3d-b471-0a15fe02b092 | -20.53998 | -56.15094 | 2025-09-21 05:53:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c22014fb-17da-392c-87b1-35175fbedeff | -15.81643 | -59.51433 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f61ed92f-6d41-3bca-b298-e4fd90d4bd5d | -15.92548 | -59.43999 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README45.md)
