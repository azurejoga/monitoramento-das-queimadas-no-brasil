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
| 3ea1df4d-8def-37b8-99f5-26d3c2c21203 | -6.66849 | -60.12555 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdd746c4-f688-39c2-a6f9-68f011b5a14d | -5.56786 | -56.18288 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2597a3c-fe92-3881-a4ea-3fbfe6a0ace7 | -7.29129 | -52.36874 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46718bdf-477a-3114-ae8c-0e1da312a650 | -6.25007 | -55.48421 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e05177b-34b8-337c-a998-635f52a9bf91 | -1.60334 | -54.40466 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95b3935d-6256-3bf0-81c3-f10e6405fc7b | -6.18446 | -44.93751 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5749f7f5-4387-3379-9cf8-c18dcfeda5ba | -8.37792 | -45.76455 | 2026-08-31 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61c9bfef-d02c-3a5b-91e8-6e791d867e72 | -6.25106 | -53.67214 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cce37ba-067c-31e6-a166-127480ec19b0 | -6.26344 | -55.37738 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3780491b-94df-3329-9244-fd5cc322afea | -7.51303 | -55.28148 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ec02557-3b4b-3ab0-90b6-c5bf97b0040b | -6.10843 | -57.86571 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d20928e5-c3b0-3619-88ac-ac257a9b4a1d | -5.88366 | -57.77562 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6bdad44-a66e-3c86-b218-53984a1aed3d | -6.25052 | -53.67562 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15eb26e1-39a9-3840-becf-373ef0afb069 | -7.61921 | -55.2988 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ba8967-602b-3799-a5cc-8ebdab754ee3 | -5.57943 | -60.23092 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5fc3f76-405f-300e-8207-003f2398fb7b | -7.31159 | -60.58629 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 394e6a5b-dcb4-3d68-8888-5be1d96fef5e | -6.18122 | -44.93575 | 2026-08-31 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44677ba4-9d5a-3fe6-b8de-cb5097038ffe | -6.24896 | -55.42591 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c05a62e0-9a48-3d37-bdf8-9ddc5a4b81f9 | -5.2448 | -55.89647 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8518a511-20a2-31b2-87c9-eec4255aba0f | -7.11209 | -42.7611 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b4d927a7-6991-3120-9cc7-52b5671dc479 | -5.88506 | -57.76688 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8208b21a-075b-3bb3-85e5-da54421c56ad | -6.53312 | -55.11095 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f6fa40-854a-37e1-a21a-29957cd82271 | -9.43747 | -45.67252 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d658b61f-a87b-3c78-8687-db6c0c0a2aed | -5.88137 | -57.76633 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb225423-4452-38db-b810-994076956905 | -4.66342 | -55.93104 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e523272a-ac89-39b9-a2e5-6471020c42c0 | -5.9849 | -53.6128 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91745450-68a1-30a1-9825-b593839e1de3 | -6.95078 | -55.69823 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b45dcab-ff09-37f2-a31e-d126abab0a86 | -6.12594 | -57.69106 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4e089b9-c69e-3daf-b7a2-0e812eb86f57 | -6.93413 | -55.62991 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6fff2ab-b5cd-3309-862d-299a5290ed24 | -7.27866 | -49.83433 | 2026-08-31 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cbe519c-1102-3ee3-b5b9-018943dadff4 | -8.41304 | -44.98562 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aec3e9e-096a-38b7-beb4-b8761ded5eaf | -4.85693 | -55.83939 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df1cbbd-ab60-3524-beb2-5e495c1dea71 | -6.94966 | -55.70536 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bca549b5-b441-3ad4-84a6-f18e656abd60 | -5.89708 | -57.75877 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d091990-6e77-3459-9922-9aebfd5150c0 | -5.61026 | -44.00536 | 2026-08-31 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0bcecf3-338b-3416-a7d0-92e99c4c9df0 | -5.87998 | -57.775 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ee0ea50-b0a2-3e54-866c-c18a02fbc682 | -9.43571 | -45.68636 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae4bd652-4aad-3ea4-9363-56da25a468eb | -8.23975 | -49.04199 | 2026-08-31 04:57:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdf00442-8498-38ba-8451-399fe9a583d8 | -1.62062 | -55.17042 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b599be3-6cfb-3aec-9abb-1caf76e547d8 | -9.42342 | -45.65335 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a3270a-61b1-3948-bad9-bc8fece5aea8 | -3.79796 | -59.60789 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12accb46-6a24-386c-864e-fa2627cba944 | -6.264 | -55.41737 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963ad224-3ce2-31b6-9066-9faad842b227 | -7.93032 | -44.24983 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 381ecfc1-9105-30de-a88a-67f54d9cd8b7 | -1.6 | -54.40412 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbe6be64-7fe2-36dd-b69b-71b0b8350ef1 | -5.88531 | -57.7614 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 517b6c67-3d62-3294-bbfe-44db6e566b47 | -5.25609 | -55.91333 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cfd8595-45fd-3e7b-95f0-bfc9aeb94e74 | -6.21267 | -55.48205 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c67f33-b7bd-34d7-94bd-4cf728cafa96 | -6.12032 | -57.67853 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| efebff4a-ae9e-3b29-94ad-a4208a98e16a | -7.61104 | -44.88428 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfc0d51b-7338-3356-bf90-f22098d7a636 | -5.57842 | -45.73984 | 2026-08-31 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 767b57fb-7ac7-33ed-8c1c-7e9b3fa3601d | -6.12074 | -57.67717 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 5e46bb56-ee4a-3b1d-a1f7-d30922d0bdc7 | -5.26007 | -55.91026 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c284c003-d713-3f5b-84c9-cc2cdb99d295 | -6.26234 | -55.42796 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7292858e-a679-3c82-9f77-db064dd281ae | -9.42384 | -45.65003 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07061c31-c671-3c82-9629-b3f8a2ca4e2b | -5.3216 | -55.85226 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b25262c4-6dfa-32b7-96a6-b64e13076d26 | -6.31846 | -54.74541 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27511606-4996-36af-bbac-fe4c6fc91c88 | -6.09864 | -57.69687 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c7bbd2-95a2-367c-815d-c184dfe6e69d | -5.25561 | -55.89439 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 964d5478-a873-3a7c-bc11-f8870b1e4e63 | -3.92041 | -61.32108 | 2026-08-31 04:57:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc59602b-e179-3753-afe3-24421174550b | -3.72059 | -51.16877 | 2026-08-31 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58e57d64-6f65-3d2c-a287-c5e3c01bd078 | -7.19193 | -46.56865 | 2026-08-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2b15758-33fb-3cbf-a23c-1825584a9f3f | -7.31517 | -60.5912 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c5879b-b738-30d3-b862-e18d6db7e35f | -6.93692 | -55.63399 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d1124f03-218c-3413-8d60-141426b7489e | -7.62294 | -57.61927 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d365b637-5cac-361e-adf3-c67b0893058e | -6.67937 | -52.84969 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df913cd7-49b5-3ab0-9798-d1dca7e0f1d8 | -6.15057 | -57.88591 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f512d49-a3ce-3abc-bb35-3afe82d76e14 | -6.62245 | -53.17895 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ccad86-39ec-39f2-b7f5-dff676f901ba | -7.61035 | -55.29025 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d898e0f-6d5a-3909-9d3e-a90fd9c980ba | -4.15088 | -60.70358 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fb9af91-d3d1-332c-9b66-95808e462df3 | -6.24999 | -53.67911 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7bdd62c-8e8c-3e12-a237-10080d8e387a | -6.2601 | -55.42038 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4702cec-98f6-38d5-bd66-10d66f747ac7 | -7.94187 | -44.25185 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d0c666-7b0d-3d6d-9db1-ca5767c46b60 | -3.63422 | -60.55269 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b76f8d66-2511-3060-b3f7-86828025f98f | -4.96716 | -55.85302 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1620dcc5-7010-3362-9f44-ff7f679e0904 | -3.88809 | -59.39771 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a5d900-cdaa-3c7c-8c73-b381d564b9fa | -3.69166 | -51.99656 | 2026-08-31 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65a5cf35-73a3-36f4-a4f0-139e3550521f | -6.11219 | -53.86678 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c73119c-804b-3efa-9283-43ba39beb207 | -5.57876 | -60.23502 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6457dccc-2ba3-3597-adcb-73c04f33f5fc | -6.95357 | -55.70234 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3f6c1d9-42dc-3141-a5e2-de5ef9c4c3a6 | -4.97345 | -49.61489 | 2026-08-31 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d428fe0a-0207-3402-8609-caa2b7d57877 | -5.3182 | -55.85172 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a88268c4-8a95-35c4-a299-eb59ab888308 | -2.98178 | -60.9251 | 2026-08-31 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 884050df-de1c-3f4e-8b35-f196d1f6d0c0 | -5.48648 | -57.14577 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1805646-efb3-39c6-bee1-edf22df660ae | -3.6911 | -52.00021 | 2026-08-31 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df51d45f-2be5-3fc8-bb83-2d897b25c4f6 | -5.25103 | -55.90121 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9f95a00f-8a0a-3844-b658-b95a9a8b4b72 | -7.28784 | -52.36819 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30d6e2bb-a75a-3d0a-a124-c0d53987d5e4 | -6.37424 | -54.95387 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 865290b9-1169-3b31-b05e-dee0a53c6039 | -6.07837 | -57.89391 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c42fbed8-589b-3551-8bcd-b42d355dc561 | -10.757 | -54.00104 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e9c6189-c7df-3202-ac57-85c005abe9d0 | -14.12865 | -52.80916 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac694f9a-d9a9-3ccf-a0ce-d88ec0dff583 | -10.74319 | -54.04698 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2adcafad-e6fd-3fde-bdd8-4d919de35136 | -9.22046 | -59.7597 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c65a920-e936-3cfd-a198-d2161663b2d3 | -13.83664 | -54.02008 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d31ec676-eac0-30d0-b092-fcea1545fd03 | -10.15013 | -45.75784 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa2fe49d-d303-38b4-90c8-fdc2ba7e8a17 | -12.40117 | -46.45126 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4290fddb-fd81-35e1-a122-f14c08f8c922 | -8.77803 | -62.45187 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd08182-c4e9-35f9-b794-3394163c9966 | -13.18318 | -55.66336 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b525e176-a24b-303c-83e4-49f6121acc30 | -8.80002 | -62.49321 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 787afd0c-dbdf-3b7e-a0e8-11a53b45d2c1 | -9.19115 | -51.55278 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50fe2be8-2c64-3fb0-9e23-5a9b81a0fcf6 | -10.747 | -54.02169 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README45.md)
