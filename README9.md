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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92d5fb65-1cd7-3210-9026-4c3f7a1ac86d | -10.94205 | -49.44644 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 572815f7-54bf-3600-9ab9-76604d51da79 | -10.66768 | -49.70578 | 2026-05-08 05:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b99acdd5-e58d-3d8f-b637-c7d42a008982 | -12.34698 | -50.03067 | 2026-05-08 05:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62c8efc6-ec52-3968-abc8-029880dd6e4a | -11.60293 | -54.1862 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18a012db-5a13-3384-97f4-aa6fc1fcf1f8 | -9.56124 | -44.57305 | 2026-05-08 05:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b8a9518-7266-3479-8a5f-7748eedc9b3a | -11.60674 | -55.3278 | 2026-05-08 05:08:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ece70a1-649a-3ff1-b7f7-852710916aaa | -11.82184 | -47.34027 | 2026-05-08 05:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9311c13b-f44e-3054-ba24-10a36f92e58d | -14.13564 | -45.37983 | 2026-05-08 05:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edb9150d-f27e-387c-81de-7d00bb7d0027 | -11.84422 | -57.84694 | 2026-05-08 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d39df4-6b69-30e9-b542-20d0e84cd488 | -8.71211 | -49.08308 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b476ca4-b58d-31ee-b514-6cd3d54b8faa | -9.56401 | -44.57369 | 2026-05-08 05:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ce47aba-84f9-3b94-b9eb-0b866cdc7a57 | -11.30794 | -54.03339 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d40fcfc-d6fa-310d-8631-8e9b9147c141 | -11.47052 | -52.92123 | 2026-05-08 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8b2a95-3975-3fad-b81b-a0bfa8fd9ded | -11.80388 | -56.99208 | 2026-05-08 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72645814-018f-37e5-9203-243f47f782e9 | -8.69677 | -49.09102 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd36936f-96e3-3350-b7ee-05aeef043847 | -10.93924 | -49.44792 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a01796c3-5cb3-3f80-873a-972e20a0a201 | -10.0485 | -51.67747 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed9af9b8-94b4-34b0-8764-91c5f19666f9 | -11.84089 | -57.84637 | 2026-05-08 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d659ee01-fae6-3526-8bd8-78be75954e05 | -11.83756 | -57.84582 | 2026-05-08 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed9524e0-1616-3567-a94d-e268a1b63b0f | -14.19771 | -57.42364 | 2026-05-08 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ef30c7d-f14e-3f13-8378-1d2702e05c65 | -10.05 | -51.66705 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e3fbfc7-b033-3093-b34a-af0663a7cfb6 | -11.64503 | -58.25714 | 2026-05-08 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355f25b4-8399-3d47-a183-a6334c5bc540 | -13.48253 | -48.91809 | 2026-05-08 05:08:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1b230c0-17fe-3a4d-b2a0-486c4f5de7cd | -11.75035 | -54.79322 | 2026-05-08 05:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f761b91a-a0ad-3595-b0dd-57bb14169256 | -10.24165 | -52.22905 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce749c37-be7d-3468-bd6e-ab2748aed1b2 | -8.70745 | -49.08253 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f400152e-61c8-3cbf-a37a-3b275ff2e4e1 | -12.15382 | -46.66535 | 2026-05-08 05:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70a645b2-173a-3b98-9788-90ed03088374 | -15.6154 | -46.51254 | 2026-05-08 05:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8c68883-5dd1-366f-a71a-8202f6d9379f | -9.30984 | -48.58154 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa44095f-f650-33db-85d5-046e457f9337 | -11.80719 | -56.99262 | 2026-05-08 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e5a8c00-d67a-36f9-a75e-dca838860ff4 | -11.84146 | -57.8428 | 2026-05-08 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d756ceb3-9172-36f3-8354-f8c0dc4bd57d | -8.69417 | -49.07577 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d455aa5-73fa-3fb0-a0f8-6c96ecc8f4f0 | -14.3181 | -57.73507 | 2026-05-08 05:08:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc3ff2d6-0b3c-3555-b964-f745b766a895 | -12.85928 | -43.75883 | 2026-05-08 05:08:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1190714-09be-34ac-b88b-574644edc614 | -13.4775 | -48.91741 | 2026-05-08 05:08:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3aa61b39-8895-34a4-87f3-b598628ae411 | -11.7905 | -47.09521 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48ad95e3-b166-3059-9d30-f0cf4b32ebf3 | -9.30423 | -48.58635 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef42922a-6a1d-3e20-9d0b-b39864b72ddc | -12.77169 | -59.00574 | 2026-05-08 05:08:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e5bd231-f757-31b5-a089-88180bea285e | -12.34762 | -50.02591 | 2026-05-08 05:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dd977f88-fa10-3f3f-818d-cbe0ce603dcf | -15.60832 | -46.52143 | 2026-05-08 05:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2dc74e7-4b48-305e-9deb-52b4a420b1f0 | -12.42572 | -54.21674 | 2026-05-08 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14f34446-9ecf-39e5-9671-8fd805799893 | -11.62906 | -47.88858 | 2026-05-08 05:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4af0ce-b1b8-37b6-be55-3ec3e11c12ad | -12.14927 | -46.66336 | 2026-05-08 05:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1791bb9a-589d-3437-9b99-fcd36204f5d3 | -11.29396 | -54.75655 | 2026-05-08 05:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd29f8e9-7d1d-360b-a654-5b402f21fddf | -9.56059 | -44.57808 | 2026-05-08 05:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13a3ccaa-9a80-36c9-9a52-eccb06ba6440 | -14.13963 | -45.34286 | 2026-05-08 05:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2127c293-cf88-3812-9eab-9bd72e81c324 | -9.24625 | -60.33397 | 2026-05-08 05:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8431013f-f0ea-38ff-8989-1a2b50f52863 | -15.61489 | -46.51725 | 2026-05-08 05:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e8d7662-e69f-3007-9f14-0bb1a0a1daa7 | -13.36734 | -54.26755 | 2026-05-08 05:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49347232-9b02-3e87-b88a-7883e568d56b | -11.6299 | -47.88203 | 2026-05-08 05:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9308567-71ed-3a39-9568-b95d70680930 | -8.69485 | -49.07091 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e488d45a-289f-37e8-a964-508929f8a901 | -10.67489 | -49.68742 | 2026-05-08 05:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92a84960-ea40-34f3-9415-b1ad56d3c434 | -10.93583 | -49.43741 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfb1e183-cd70-3516-974e-6ca31cd1cecf | -11.47428 | -52.92178 | 2026-05-08 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b535ff55-f474-36c4-b0f9-307d85eb0707 | -14.20489 | -57.4212 | 2026-05-08 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe7558fe-522b-3ac2-855e-02989a81314e | -11.75093 | -54.78938 | 2026-05-08 05:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4225a67c-219f-3d22-b907-baca93cc29c0 | -12.14919 | -54.64556 | 2026-05-08 05:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 754ff651-8a17-3c6c-b0f5-72a807cb9765 | -11.47871 | -52.91772 | 2026-05-08 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37fa7d1e-8672-3002-b70d-4ce59bc5f573 | -12.14807 | -46.6647 | 2026-05-08 05:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca41ce79-aeee-3eb6-9dc4-d70203bafc2c | -12.14879 | -46.66744 | 2026-05-08 05:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 401cf66b-304a-3c36-aab7-7d3d25eca679 | -10.66833 | -49.70103 | 2026-05-08 05:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69fdeb6b-cd06-33ef-8a78-fccbc93a2093 | -11.64167 | -58.25658 | 2026-05-08 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89941922-6140-3bee-bcee-4936a9b7494a | -11.76577 | -43.65056 | 2026-05-08 05:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdce1a87-fd65-3c31-a949-4b2014b0c732 | -8.69882 | -49.07644 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f91156f-ba01-36bc-a567-d542864a9c4b | -8.69609 | -49.09584 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 671e9351-693c-301c-a1f8-19e98e027b1a | -11.61119 | -54.1792 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e874d061-0b5d-3b32-99e0-ec13f9a81a3d | -11.80163 | -47.09655 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f9c8dc8-4af8-3220-8bf9-ec511212a51f | -12.41602 | -49.6708 | 2026-05-08 05:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c271745-2644-3886-8a4f-44a1615dd7aa | -11.84653 | -55.01405 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 406ba958-030d-3edd-ba54-6ed08a926046 | -12.85236 | -43.75797 | 2026-05-08 05:08:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18f1aacc-7d4f-36b9-9664-0c8609b7fdac | -10.23394 | -52.22788 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd950a9b-c155-3ed5-a8ff-c22c82e280cd | -9.29451 | -48.58504 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76574c18-d439-3306-9cb8-7015e04794fc | -10.93804 | -49.44089 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a29165-4ee7-34f9-b15d-09692df29d41 | -11.82229 | -47.33673 | 2026-05-08 05:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ffa9761-da64-348b-93de-a9ee19afb91d | -9.29937 | -48.58569 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 724a1892-a169-3a85-95d6-6895a3f980c5 | -12.41476 | -49.66885 | 2026-05-08 05:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83671924-b4fc-3de4-8780-d252bec2decc | -9.41342 | -50.6888 | 2026-05-08 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06b248e9-9fcf-3530-b954-21007fccb6d4 | -11.82139 | -47.34378 | 2026-05-08 05:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ad8e39e-5789-3f3e-9512-b52d16b14cae | -14.14653 | -52.89225 | 2026-05-08 05:08:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4011851a-1822-30af-926c-2dbd454a006b | -14.17596 | -52.88109 | 2026-05-08 05:08:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27a5cc3c-15aa-3890-ade1-ff5fb7ea65a7 | -12.41129 | -49.67022 | 2026-05-08 05:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 380a7234-438a-3cd8-9145-556f8f547fcb | -11.79652 | -47.09211 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e318f561-9825-3b19-926b-6b8a5113d256 | -12.85164 | -43.76457 | 2026-05-08 05:08:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83296362-2b76-3aaf-9e91-3c2ecd13493c | -14.13323 | -45.34209 | 2026-05-08 05:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33e0df5b-75e3-3593-a237-4e38b15a5961 | -11.62948 | -47.88532 | 2026-05-08 05:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee264c1b-acc3-3369-a947-bf5ff5ec543f | -11.31089 | -54.03796 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8967e55f-5825-3e4d-86a1-d8519b02f787 | -10.04601 | -51.6665 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 634222a9-ad40-3f05-8c1f-5d57be12985a | -10.04202 | -51.66591 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3311cf-290d-3577-8b4a-abbed171a133 | -14.19439 | -57.4231 | 2026-05-08 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c749c7b-15c7-3820-94cf-1a81f4f1efea | -10.03804 | -51.66533 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f29fee4d-a32d-345b-ae74-768c53a07cc0 | -10.03729 | -51.67054 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e43174-f36e-3625-b2e5-8b8d7fae3787 | -10.04925 | -51.67227 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d11e540-e28c-34a0-b906-78bf15a95fcd | -11.06731 | -49.47218 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3795ae9f-14bc-310e-889f-3822cb874a58 | -20.22181 | -46.82809 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd8aac93-3852-315a-a9b1-cc5befde7593 | -20.22139 | -46.8327 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b6719ae-bd36-33d6-86df-983b2a3a9604 | -16.15446 | -58.4877 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb82c513-6e0b-3a3f-ba3e-794a56d8469d | -21.70391 | -48.41645 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a86904f7-91cd-3543-b738-d56932b562a3 | -18.51118 | -55.51253 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7cbcf2f5-842a-30d2-a0bc-d1b694426290 | -18.50992 | -55.5107 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 91961037-85a0-3fc2-8d37-6ae079bdb8cd | -20.72063 | -55.174 | 2026-05-08 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README10.md)
