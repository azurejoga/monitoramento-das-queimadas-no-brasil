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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed2e4fa-8aa4-35d9-b8af-448d417d57d5 | -8.12424 | -62.88343 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b2b444f-3113-3a58-9bf3-315222456d14 | -11.04527 | -49.13305 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b1785a7-a4fa-31c6-a65f-d6822ba0e0a5 | -12.7494 | -48.10512 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f7181f8-36dd-3825-94c2-4a15f3b230f5 | -10.41786 | -47.16263 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb0b7457-4941-365b-b0b0-38e9fbad67d9 | -9.20654 | -59.49575 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da8556cc-5257-3229-b25d-689edef44575 | -8.63225 | -62.65033 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56930017-9c88-39cf-9bbe-e74a736751cf | -8.07164 | -49.65714 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5888892d-478c-3d9c-882a-6d28578bed10 | -8.07167 | -49.67857 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2fedff-defa-3290-bcfc-feea9bfc9b44 | -8.8131 | -45.4617 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d73f8a71-9ff2-3493-91f0-ea5f29beb6e5 | -10.78926 | -55.45115 | 2025-08-25 04:42:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea41c7d4-db36-3baf-aa06-db90089450cf | -9.86825 | -47.83824 | 2025-08-25 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a45f908c-1b45-3828-89c4-54cc6e6d42bc | -8.22731 | -61.39139 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f914928-d6c7-3d55-8823-09c82f11eb13 | -8.61067 | -62.6021 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78cd89f4-881a-3f7d-8338-f928ed22c0cd | -9.19775 | -59.50869 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e858a64e-241e-3f32-866e-b9f34d5e0b16 | -9.20983 | -59.44205 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0784e5ec-48b3-3570-b6b4-1fd3a505d71f | -8.59064 | -62.63462 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61873cb8-5306-3b40-a529-2bf4962cc38b | -9.17581 | -60.81667 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec944606-5201-3f50-9bf7-116c04fab3f9 | -6.8263 | -58.96015 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1361cab-996d-3915-823d-3f4d7c0c5c08 | -10.71777 | -48.31129 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56afeda8-d7a8-374f-9cc3-af53936b4f46 | -9.20389 | -59.50981 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b91f7ac9-70bf-3237-849d-d843c4cd8b9f | -9.64966 | -59.63827 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2eea61b2-a553-34b5-a3ee-8583622d0a9d | -11.27604 | -44.96261 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6546bdc-6d1c-3130-bb13-66374e0662ab | -12.73707 | -48.1401 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 588df6e8-d038-3542-b66b-57b28046bc87 | -13.4467 | -46.88345 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37e318e9-de30-3f2e-bb41-2a875116480a | -9.2295 | -60.92287 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9e6ca1-b607-3797-9469-93d897061620 | -12.29553 | -49.1456 | 2025-08-25 04:42:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20317f42-0235-3100-b795-ac5f6e19888c | -9.51491 | -60.51276 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c2cfb5-b7db-3093-a096-6929fd5ce7ee | -13.63042 | -48.154 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274ba41e-2e94-3772-9c68-12562db2cc88 | -10.47146 | -48.32483 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 103d54eb-9600-37d4-ae82-c5b2341f9fd7 | -13.81284 | -45.88731 | 2025-08-25 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83ba28e9-3e73-34ac-b66d-28fdbb70d68c | -10.25542 | -59.10271 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7da6b5fe-89f6-3e0a-92ba-4626cd5283ea | -13.45082 | -46.9098 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aef6167-f97c-3322-9723-bf68cb1cdc9b | -12.75179 | -44.41986 | 2025-08-25 04:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34f54ca9-fcfb-3bea-ac8b-33587f4f76ff | -9.14853 | -59.46999 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83f3e50-b1af-37d9-a361-3248049bfb51 | -9.19135 | -59.48193 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f769f77b-bf0e-3942-a383-7d43421506f8 | -13.43695 | -46.92614 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfa89db6-59ae-30ad-93b6-8cfcae97d46f | -11.19891 | -48.46734 | 2025-08-25 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a4a4bd5-0fba-3fd9-9d72-ee77e47b95aa | -11.27246 | -44.98866 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98f679b3-b7e5-3efd-ad61-282a4414fe3e | -8.11062 | -62.88071 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72212f45-93fa-37c1-9234-3d19d51cb81e | -7.90446 | -63.07164 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a0b6bf09-baaf-3102-bc8e-40fc596d0a0f | -10.78571 | -46.43067 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06cfe11-35e5-307d-9815-62cd90b012e9 | -11.60306 | -46.3596 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| aeaf6d8c-f66d-3231-b9f0-74c251822cd8 | -9.20488 | -60.92244 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7ec7bfc-aeb4-3e97-953d-39a01e2d818b | -12.75292 | -48.10579 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f50d029-8a73-3d09-8c7e-a59aea9b95ce | -6.82209 | -58.95317 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1eef9eef-3c7b-3d47-8fad-ded6fa20b347 | -9.1741 | -59.60781 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fcf9cf1-e31c-39ea-88e5-79dc9d965ad7 | -13.61676 | -48.17284 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 022f1be1-ed98-3515-b04e-8f2adde5f715 | -9.15175 | -59.45256 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7bc828b-553c-3641-b0a5-30020353ed4f | -12.75112 | -48.11814 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf1941da-4ed0-3b98-8b4a-2beb7c88f2af | -6.83244 | -58.95859 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2898042e-b44e-36be-91b1-e529be7bae1f | -9.74174 | -47.93701 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1230725b-a0ac-3900-92f8-610a4bbb36d8 | -9.20255 | -59.51334 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5326cc92-4313-3e27-a037-5e65c2cbd990 | -10.88654 | -55.79802 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1ad6301-aea9-34d4-ba03-a2ee07a9243b | -9.16027 | -59.49793 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3c815eb-a555-3903-af00-a5bc19e061b1 | -10.7164 | -47.12809 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29799de2-51bd-3247-b951-41aa9f06e760 | -12.75466 | -48.11862 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71b50e12-059e-3940-8747-75781a8a9d34 | -6.81644 | -59.4295 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50a16db0-afd1-3609-883b-c77d756544e9 | -8.5109 | -63.87909 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f5b684d-f16a-348f-873a-60a7d574ce4b | -8.43166 | -48.25673 | 2025-08-25 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b79b051a-1246-3d89-ab18-21a5aed3ab17 | -9.15265 | -59.47813 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d254eb4-5539-367d-883b-2d111ccc9ee7 | -7.65514 | -63.53242 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22141338-f65d-3647-aeab-20c38da266e1 | -11.5941 | -46.36781 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2a17474-1c4b-3dbc-833e-77b3c3d17986 | -13.00783 | -50.55664 | 2025-08-25 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fb04a52-200f-317f-81f6-f26441b9196b | -9.61518 | -55.35178 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d50d2a9-a01b-3deb-832c-34924087bf3f | -6.69224 | -58.85577 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc5dc75-a2eb-33cb-8e4e-da978687e7e3 | -13.46052 | -47.00621 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b58e1ff6-3238-33ec-8e3f-01c11ac99bb5 | -10.03129 | -51.07778 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb60088-7661-3468-967c-67f308d8fa86 | -9.19935 | -59.46889 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 496e96f2-ad04-3c05-8244-17111e3d374b | -8.49657 | -63.87626 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b0b90d2-756f-3655-ba0e-06a4c432e60c | -9.56491 | -48.16702 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7bde0e4-78fc-35c0-8dc2-9b210cf9a7c4 | -10.24436 | -59.66316 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 70f773a4-364a-351a-81b1-06b3f411f67c | -9.18159 | -60.78658 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 72d9965e-da4f-3581-bd79-f247c41572fa | -9.16311 | -62.35415 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27241786-aa41-3b76-8db5-864f3cea5b78 | -12.75878 | -48.11519 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 813df966-4abf-304b-b815-e93140a074a9 | -13.15612 | -53.73737 | 2025-08-25 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21a82c2d-9625-3005-8c7b-8a0d395a644c | -9.21278 | -59.70484 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954ff9e3-c896-358c-85b5-91050913d5b8 | -8.32124 | -47.25673 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 550aed4f-8be4-3aa9-b901-38338be054aa | -12.74824 | -48.13775 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c77bc8c-4241-3f7e-8a34-0c294fbd410a | -9.16456 | -60.82714 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| efa01218-4ed6-38bc-a3c6-fc40455231fe | -9.68849 | -48.33765 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c495b1e0-dd8b-33de-bc36-3c21fd7c7771 | -9.80065 | -61.20412 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea2a934-1853-33a3-a28d-c3cdcab3dda8 | -8.13499 | -47.29712 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f19ec7c7-a9c0-30ba-9940-40d19e3379b7 | -11.14347 | -44.73985 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfe9bef9-a636-3d2b-bb92-6c194c06fdc8 | -8.88647 | -62.44181 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e3511dd-2cb8-385c-a393-406250055f78 | -6.8011 | -58.63003 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f69135e6-2561-3e2d-83ad-49dbea03a241 | -9.21819 | -59.67575 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65fc29cd-28e6-3c35-9178-7a6931a289db | -9.65034 | -59.63464 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22e98e85-57a3-331b-bdf5-6d81717ac096 | -13.61556 | -48.1811 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2128615-ab7f-307b-96ef-5e17b5bed7c6 | -9.57154 | -55.37072 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77dcf46b-7010-3402-8167-c5dea49ac5d8 | -13.50994 | -46.90231 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab2cf0e6-377b-34fe-bfe4-a8eabfe8385a | -8.32064 | -47.26065 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f87b9f5-08f2-33ed-9112-798f0447594b | -9.19348 | -59.44586 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb30add0-c5fd-346a-b93b-191b3a3b0be0 | -9.20456 | -59.50628 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57efe210-d658-372d-a247-985e005c70c8 | -11.46132 | -55.4682 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 19b441ce-2a05-349c-801e-9ab52aa7e202 | -8.05947 | -49.67316 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18d4767e-8c0e-3e4e-9380-06c07039a48a | -13.4822 | -46.87908 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd1c2c0-f5b1-335f-a1af-9474d2c0426d | -10.10619 | -57.77177 | 2025-08-25 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42d812a1-74ef-3564-9ff1-cbe7a61e1f44 | -13.28827 | -47.51298 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc7d189c-6a94-3fd2-9039-b0d356eb56bb | -11.17824 | -55.02665 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ab9257d-3ba2-303b-b777-27ffd7f70bb8 | -8.22161 | -49.56358 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
