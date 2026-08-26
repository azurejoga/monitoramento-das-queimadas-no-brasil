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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2abf1bb1-9332-33aa-bf1f-66a013b90c0d | -9.16542 | -58.33435 | 2026-08-26 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 652cdbf1-3045-3383-8e26-92e363da5db0 | -13.22869 | -51.37265 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 26df56e4-c130-36c4-bce8-ccd418fcae74 | -14.12807 | -52.35629 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf15afa1-2a4a-300d-9e62-91318160ecc5 | -14.34865 | -52.9943 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98a86ad2-e7b4-3b48-aafe-0b2765d1d908 | -11.79298 | -47.64392 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1d53766-9f6f-3f15-9e0e-338384522cc0 | -10.16688 | -55.30653 | 2026-08-26 04:53:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f81d23-8805-39c3-9df9-7bf29cd6942d | -15.14611 | -50.05774 | 2026-08-26 04:53:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a66dd4f-a044-35a3-adeb-1386aa099852 | -10.9902 | -60.79325 | 2026-08-26 04:53:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35511d8a-8d3b-394b-ad12-85294abc389b | -13.17224 | -51.34045 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 729b32c5-b782-392a-ac4d-ddf374773a60 | -13.22157 | -51.37157 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9892476b-157c-32b8-8784-802a6fe5e891 | -11.54823 | -46.97677 | 2026-08-26 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c61d6cae-598e-3b9d-a3a9-b7590f3acb1e | -14.79314 | -48.80739 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7a19425-1202-3531-ab29-5baf72505568 | -14.79879 | -48.79705 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a6852230-5b9c-3400-91ea-2ab4ba25fd02 | -13.42181 | -57.07416 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e819a3a-0b1a-34af-94dc-fcf1a9853775 | -9.1114 | -60.39466 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 059469f3-a44e-3693-af36-62d1512bbf44 | -13.60931 | -49.0146 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 474fb202-481e-325e-b49c-a9661414dfbf | -13.22216 | -51.36744 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a4015042-9654-3ebd-b130-f47d181ce239 | -10.7476 | -54.00487 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78ec5e28-971d-3e8e-a25e-aece94483280 | -10.76802 | -54.02608 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c53b9a3f-dea3-3f16-a234-6f9bdf5b91d5 | -9.17002 | -58.33149 | 2026-08-26 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8d87709-2391-3c4f-a23a-9aa5b34e31c3 | -14.49098 | -56.47853 | 2026-08-26 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0842f38-fd76-3e0c-b70a-7b0555b659a1 | -9.20194 | -59.57889 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff621e0b-faa9-397b-975d-423c25492813 | -15.60833 | -53.12235 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2ba92aa6-b2d8-3555-b339-e85f3140ccba | -14.36889 | -51.75893 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b98bfddf-9be0-362e-b895-36c112eae38e | -12.64446 | -48.40483 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cca70d7-16fd-3a05-ac90-9c5cda760cc3 | -12.65286 | -48.40612 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2521937-c550-38e3-a0d9-bbbedb7a8572 | -12.6592 | -48.42295 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0deee164-8f54-32dc-a52b-178f898ebd87 | -11.84584 | -47.68132 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e0f4e2d-7b13-3de7-b8a8-57d6a6e97cbc | -9.6043 | -55.11726 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9b6c5764-3d80-3c19-8102-eefe4341f010 | -9.9676 | -53.94674 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7e0b237-2498-3d3e-8d05-2472bbd324cc | -9.66895 | -55.08254 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c52df96-a20b-375d-ac08-a190805b01a2 | -9.65306 | -55.09505 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e7220c6-a5fa-3ffb-bf5b-d430b7d93ee2 | -13.24635 | -51.52615 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 250033c0-3d23-3467-b89c-4d3ba5ce23a3 | -15.60377 | -53.10621 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb5293fb-290f-3da0-91fe-99cf2f3bcb57 | -13.35152 | -54.3776 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80595120-98e9-3ee1-85ec-b0e50c8a54d6 | -8.82217 | -62.32977 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f85d0243-d5ee-32c7-9b9b-8746a46ae517 | -12.75535 | -46.45955 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f247cf2f-ca3d-3862-b8ad-4cdfb4bc906b | -10.00372 | -53.95601 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34dea7ba-cd15-3ee9-aad4-a9b0c698c074 | -10.76637 | -54.03658 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 66cc1d31-5658-3581-9f1a-2a30694083a8 | -11.48894 | -45.10928 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1d55c59-dfef-36a0-ba72-d1efcd4ac935 | -11.25712 | -47.05458 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 230d6da8-4323-3adb-9c2d-4844145911c8 | -12.75901 | -44.26819 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 128bb3f6-5889-3577-8179-6809b7e9dbb1 | -10.42648 | -61.22303 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2512c67f-c670-32b6-b8c7-655c69808987 | -12.08525 | -64.24535 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac8a6eb4-7faa-38c5-b2d1-4f38fa8fdbc0 | -10.99025 | -60.79577 | 2026-08-26 04:53:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2a53bce-f75b-351c-9122-f784f59a3ad6 | -13.66266 | -51.84794 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe5f79f3-ca32-3125-8214-792804b60535 | -11.19659 | -55.08082 | 2026-08-26 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c43ce30-f07e-391a-b0e7-8777276438fd | -14.44019 | -53.08419 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2b96245-a635-3775-b9d6-750f090a3dc7 | -9.48432 | -63.27952 | 2026-08-26 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20622474-7724-34ae-8424-8351a780e463 | -12.67233 | -48.42085 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a6654d2-692a-3f11-8069-b2331c5c9932 | -13.25599 | -51.38524 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5265497b-26a2-307a-86f9-83bc2d13fc11 | -12.76077 | -46.45521 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b159726-525b-3ae6-a490-b8b0816d4b6e | -14.84545 | -45.52561 | 2026-08-26 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51a879a5-28bf-315a-b36f-cd7a8a4f699e | -12.69856 | -48.41694 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ad36428-98a4-340e-b549-bee570cf449b | -13.33605 | -48.22259 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8430a5c5-8501-3c06-a136-f658b7b7a8d3 | -15.60153 | -53.12131 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8dab868d-5323-3a3e-8afb-72e1c184bb5a | -10.75919 | -54.01749 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83a4f72a-b85e-3a8e-b7e3-5249ec79a7a8 | -12.72557 | -48.37611 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2fd4107-79b9-37e7-a213-589e5b1527f5 | -9.18429 | -59.38456 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e676d4e-38d5-3f5b-8e79-5d4cb8a4b92c | -13.21801 | -51.37103 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2742741d-305d-31e7-9eee-7ac0e96563c8 | -14.39183 | -52.89755 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9994ae3-785b-3079-9cce-03009aaba731 | -13.23878 | -51.3784 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 59221cd5-5f1a-3be2-80a1-37d111c33025 | -13.34362 | -48.23162 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76ee2514-4e98-32d8-ba44-544c8f1cef01 | -15.88377 | -48.34147 | 2026-08-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2bc2f3b-746a-3361-8ab1-61d6fc729db7 | -9.46928 | -56.89997 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73f5134-0e53-385f-a78d-ab87ba0a851d | -10.9908 | -51.15304 | 2026-08-26 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f960c2-fa11-3561-ad91-14b58be909e6 | -9.48916 | -56.91514 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68242b31-f513-3d7b-8c7b-91e974c40470 | -15.57272 | -53.15147 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f83e9ebf-1c55-390a-9855-c990413f88d1 | -12.95731 | -56.61386 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8bb3611-5712-395c-8197-921f297b26b2 | -13.61291 | -49.01883 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7a1e64f-a9a4-3cb5-ba23-0a525630f8ac | -10.76747 | -54.02958 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 41ad787b-d4b4-32a2-a3bb-8b2b6383e70d | -13.3053 | -51.46685 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2122e533-643d-397e-bda6-ff858b8cd74e | -10.26904 | -50.38377 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d713477f-cced-342c-b114-a7c4699cf863 | -14.32304 | -51.72746 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fa9fc45-d01a-373c-8744-0fb1c0270588 | -11.74952 | -54.53151 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 854a8cac-3899-39c2-9246-49b5f27e31a7 | -13.29937 | -51.45756 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 5f5e176f-e59b-35fc-a2ad-7cf2e6913cfe | -11.77054 | -54.52768 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09a42e25-28dc-3317-8752-9e2980409894 | -15.59757 | -53.12454 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec7642fd-1be0-3156-86a8-3ddc99dc9a9e | -13.6511 | -51.8469 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 19863970-aec2-3539-8686-9a1fe1367ef6 | -13.61388 | -49.01171 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6258029d-a227-37de-91b5-3dcaa4978ad1 | -15.60889 | -53.11859 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8bbdde1f-1842-376b-b416-34801656c386 | -12.03429 | -46.03963 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52c5d9a9-5054-365c-83b2-167471763622 | -13.24531 | -51.38361 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f814d291-b673-3f70-9502-ca3763acc217 | -12.02385 | -46.00414 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d726125-1770-391a-9bb4-d8d0ccabb5ea | -13.86014 | -54.07938 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9942c984-c2a7-3f59-9069-a976e83b69b9 | -12.66488 | -48.41248 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eae70437-0fa4-3f5a-97a3-e362679a748e | -15.88324 | -48.34576 | 2026-08-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d49af9b1-5412-3b44-9c7a-0053c4f89270 | -9.48107 | -56.91976 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3691af11-1fd2-3b1f-a363-34dc38783afb | -9.39117 | -60.57606 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0bf91f03-7262-35d0-a7c0-80ef784a4cb9 | -11.2159 | -55.08084 | 2026-08-26 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29d93cb2-5de0-3da2-9b2e-b54b985495a7 | -13.30589 | -51.46275 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1789422d-bed6-3120-a2dc-34695b7611b2 | -11.15999 | -53.99957 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8052ec-e97c-32a6-87da-bc89103dc987 | -11.86961 | -51.7209 | 2026-08-26 04:53:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 903cc6f5-14b8-3497-9bf3-394dfa06b7f7 | -10.75202 | -54.01994 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c97a4d5-07a1-356f-901a-0defdd0ca9a5 | -9.66836 | -55.08617 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 488e4e0c-6f40-3072-88c4-a3ba301c625f | -15.62884 | -48.19996 | 2026-08-26 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0efe1ae1-3b80-3103-bfb3-887a99c1477c | -9.9717 | -53.94374 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89a850d6-a188-34f5-8f48-696290cd7392 | -14.97654 | -52.73075 | 2026-08-26 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f390ff2e-7e8c-3207-a63e-b50eb62a6c54 | -10.7625 | -54.01802 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8241b0a5-67c0-3cdc-ba01-ac9a7e87297c | -11.76998 | -54.5312 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
