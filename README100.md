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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffc89ca3-011f-3c91-999d-5401755d7273 | -4.06329 | -59.83781 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb73764d-7946-3cc7-9732-48a6eedc5c4a | -3.51516 | -54.53363 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 912a2837-4eb4-3fa3-b212-8b2afbcd29d1 | -6.95409 | -45.26568 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 248c593b-eb4a-3c09-b7fd-7f275434997c | -7.21967 | -55.16929 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f46630a-08ef-357a-96e4-75c5cd2a9d45 | -4.13558 | -54.92604 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24fce218-a237-3ca7-aed1-b3568c4ca231 | -3.2964 | -54.06496 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e9fa4c2-7f15-36e9-90a6-97a0de7d0067 | -5.81999 | -53.83226 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63ab3d06-4279-3dfd-9cb7-916ea1b611fa | -5.86075 | -53.46226 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| db7786a8-7b5c-3330-a844-babb13dfde77 | -2.72051 | -57.46248 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 021ba1be-9790-3c2d-845a-c628e3e35e44 | -9.25871 | -45.63619 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3b0d8ce2-2641-3141-9570-305267db9816 | -3.16896 | -54.72953 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae9c42ba-6a96-344e-9393-83bff16958ad | -3.32324 | -50.1849 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fac04c6-b8e3-373a-9edb-f474c3e12f41 | -3.49082 | -54.61416 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eba0cb89-0fa5-338b-a876-0158584c0ffc | -3.10532 | -53.75517 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 793b0d67-7ab2-3c5d-9e61-c84f8b5e98b7 | -3.05255 | -53.92489 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a3a23ae-ed6e-35ef-ac22-77f39797fee3 | -6.05189 | -51.73595 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed9d3dcb-7fb1-3af1-8ab6-c3eb9e32d632 | -7.18796 | -52.62463 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd02cb1c-6987-3658-b861-1a3e5f51901e | -2.88657 | -59.20313 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7fe5cb1-9d12-388c-8113-38e9a525c4d4 | -3.50292 | -51.69065 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b37ceb3b-7a29-388e-b5a3-231b6052d7ba | -3.47873 | -54.61707 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 003ecaba-b30f-30df-aa76-2dab66801444 | -6.09901 | -49.40737 | 2026-10-08 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffcba40c-c372-33d5-8d9c-e772b74bbd7f | -2.8396 | -57.48377 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f765f9a1-d1c7-3513-a67c-7e1d87ff9f6f | -2.57653 | -56.16122 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec330711-fdbe-35bd-8dc1-65023bdc5d10 | -3.48587 | -59.45844 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce733d69-34cd-37b6-a924-be6b78527d06 | -3.73231 | -55.98326 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c65b358-f3d2-3945-938d-92f4479579dd | -5.68393 | -53.48661 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b25fb3e-eb29-34fd-93a5-2534ddf7ae2c | -6.48043 | -55.29711 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f1453dd-53f6-3e32-ab1a-935bd8c6be6d | -10.42809 | -47.2816 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ad04ea4-e813-3421-8214-aaf78c68925a | -11.39349 | -46.69194 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1538cebd-2268-37ea-b180-ee25570a8fd7 | -3.09972 | -53.76725 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1fa712e0-63d7-3d85-bf3f-6e42346eb888 | -3.5725 | -54.66261 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b4e87d-2b97-32e5-bb40-54a2f1b92e6e | -3.07813 | -54.28121 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a7243bcf-e8d5-33b4-b6a7-5e055df1397c | -3.04172 | -54.15296 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d23a1d77-6e25-3929-8826-c5bda1eff23e | -10.42402 | -48.79445 | 2026-10-08 04:46:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e8a6b8a-0582-31f0-90f2-094746bab962 | -8.59888 | -53.12565 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b646cdee-258f-3e69-b115-3c9ca430e084 | -3.09175 | -58.43073 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e838ba7-f262-3c0f-a00f-e044b59698bd | -3.29813 | -53.86516 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf17d6f5-4ef8-3303-81eb-98ce89ae0795 | -5.83025 | -51.99672 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2908687-124a-3f44-9f7f-2b7238594a75 | -3.02194 | -54.14255 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f7c9006-6ba0-320a-9663-57c5b1174bf9 | -9.58635 | -48.91725 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 041aabae-3b4a-3fa4-8003-2e3d8fda9dfe | -2.99655 | -54.11148 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15f388b4-3e54-3a0e-8c7b-1036751a8145 | -6.89255 | -43.68098 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57a41c60-d25e-3a28-b30f-4665398962e4 | -5.5513 | -45.5714 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a037fa-15da-3f81-9a84-c055affc4eda | -2.7155 | -57.46895 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8eca8768-636b-39a1-bcfb-0dca648c4b06 | -5.97099 | -40.91507 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a9264ca-6516-39ee-8bf2-02dcbe3fce33 | -3.28383 | -54.04969 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0845228c-0ff7-3230-a410-276e7c4c494e | -8.37058 | -44.75774 | 2026-10-08 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2709a960-0640-38b9-8122-eb3024c53c88 | -3.29552 | -54.04714 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd4f9da6-cd11-31a9-8460-963d49415c79 | -7.60523 | -42.38353 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd455a16-2401-3653-8902-1f80495749e2 | -3.47138 | -59.57527 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e158295-525d-35c2-89f9-58436cdafc73 | -7.22231 | -55.10618 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 801be5b4-7c8c-3641-80c1-872ab11f3bc8 | -3.51351 | -59.94751 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b2a8df1-3f71-3f34-84f5-b353c09f6dc4 | -3.54296 | -54.65315 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c55cc921-7fd7-3631-bcfd-9a5f96d4d620 | -3.5985 | -54.57247 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f179f7af-1433-39ac-968c-65ebf08fa5df | -6.52647 | -55.2763 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21dd9ff9-dde1-3646-8e2e-165b71ff9dc9 | -3.03032 | -54.23433 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b2338e6-9503-30f0-b114-fc7ff4662428 | -3.33037 | -50.18249 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7523323-0ab7-3906-807a-0c2c1bc03da2 | -4.23897 | -49.98514 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccccac52-ddde-316b-b4db-19c306e1756c | -10.42665 | -47.26266 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2107dc9-15e7-346e-9839-f893d1ad84fa | -3.85283 | -51.93037 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 307fa3ba-1ec1-3420-b9d6-90c8793d0af6 | -2.99705 | -54.08466 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ff5ee141-1aab-306f-a5cf-6adf2245fc7a | -3.55177 | -50.09407 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e34f6ab-362c-31ee-b183-23becf49e105 | -3.64073 | -58.94366 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8705b08f-51c2-39c4-86b0-1d48fa39fdf2 | -8.08659 | -55.30918 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9232740-82da-3446-ac30-1dc2b768b850 | -3.02442 | -53.88991 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2023889c-1df5-3550-b86a-19a08373cde1 | -4.91162 | -49.92516 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deb805de-425e-3269-a663-f2553e6d41f5 | -5.95465 | -55.35094 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8ef2859-db22-3809-b9ee-526b17d5d017 | -3.32799 | -58.15451 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b573ab9-8749-3930-bf4b-a86db422a389 | -3.65038 | -55.50585 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f098ada-263e-3a40-b9e8-07c40948d62d | -8.98295 | -45.94758 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f9803f6-73a7-3e4f-81aa-7f2777a16b28 | -2.79869 | -54.08328 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e628c5d-987d-377f-82e2-d839c82a668a | -3.08842 | -54.26455 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0462335-f350-3924-8c56-a2b2c29b6e32 | -4.4576 | -47.92149 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a328c109-23fc-39e6-b457-095ad6414ddb | -4.36976 | -54.75438 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e17e3d3-13fb-33ee-8c0e-2116a1dad8b8 | -3.26688 | -50.70303 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e3e610-8f78-3feb-8618-68f0b0043c00 | -3.04794 | -53.90669 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f802db-58d8-3b85-ba45-477a75a62c5b | -4.14947 | -54.03634 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a234c1-9475-3dab-a7c8-38cc143ee080 | -3.15299 | -51.62148 | 2026-10-08 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7515db6f-5f65-39e0-a440-a2e68167c14e | -3.69006 | -55.48759 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a67bd419-2915-3373-8a1f-3cffc00a2d2f | -3.01251 | -54.08257 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 144e8953-5eca-320e-a9d3-2bdf6a5cb34e | -3.11047 | -53.77631 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 126f270a-19c2-3a74-8e96-22bea109b98b | -3.47499 | -59.5859 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80635efe-8178-311e-b7e4-101afa65386d | -2.78759 | -54.08156 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51f22d76-a5d5-34bd-9420-cb6f30a6fb79 | -2.99795 | -54.10275 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 326e55d5-1237-35eb-82d7-09a0527e0827 | -3.10401 | -53.76358 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72559c60-4574-3982-8274-b81fefc921e1 | -6.09698 | -53.49514 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 704d7eb1-5f80-35ca-b83f-58b91b85c4df | -3.03533 | -54.08169 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2a5ccbd-db88-32ee-a3e0-72004100ccbb | -2.50584 | -56.14227 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88380593-00df-32fe-b66b-85f74663ac2d | -2.93633 | -53.94805 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612b9c8a-22b2-3e7f-9e13-0b4ebc591f4c | -3.04469 | -53.88004 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa324135-14e7-3035-a1b1-22df2c17eb33 | -3.01781 | -54.09684 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 968f7882-1142-3c62-8f4d-72987d387549 | -5.88643 | -57.75359 | 2026-10-08 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6d43717-90cd-39ac-92c2-ea57929b6d1a | -3.7087 | -58.93635 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 726f679c-1310-3d0d-a7b3-4f2588b935a2 | -6.19725 | -51.46186 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c48ef7-8939-308b-ab21-e7beace640ae | -4.11024 | -54.4147 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17ed296b-75cd-3f3a-8f70-752daf31b02a | -5.51953 | -50.01938 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a87082dd-9c9d-3546-8223-7097e9a698d5 | -2.95204 | -54.19944 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07e3cbac-20d8-3db6-89a9-09747640ac50 | -3.70257 | -54.19854 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 632a096b-6524-396d-ba41-67b1d1fbc751 | -3.88001 | -55.99594 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6658a6b-b647-3cc4-8c97-51468a1e7d20 | -5.95692 | -55.33708 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README101.md)
