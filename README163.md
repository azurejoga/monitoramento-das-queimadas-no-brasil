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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f5673ec-2295-3b8b-bf5a-bec1f70761dd | -2.5104 | -56.25357 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14148f60-b538-3ec6-8487-15d42fe5e2ca | -2.99791 | -54.13294 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 778a615c-9292-311a-9c31-051d9fbff6b3 | -3.58722 | -59.07788 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3ba6699-1e35-322c-a738-f9445096dc4b | -3.09714 | -54.28087 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f63d6741-7f1e-3a44-ba67-8660ef9b0da3 | -3.59318 | -61.63901 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f1edf97-5020-3981-b625-68df68c303c1 | -3.28014 | -54.05554 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a973fc-7531-3c69-8e73-0393a71c7a0d | -8.61642 | -67.01976 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2e7e0d2d-c373-311c-a8e3-fbfac957d794 | -2.9306 | -54.12265 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb19ce88-8774-39a3-a43a-7197127665fe | -3.0351 | -53.93943 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3476fb3c-1762-31b4-8c9d-5bb26d7795b2 | -3.26207 | -54.0327 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 019a15af-170b-3e71-a185-62a1598da8b2 | -3.70641 | -60.554 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 572a4448-d959-396f-8760-2549e487d8d0 | -3.06336 | -54.21792 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4d778ce-b804-341f-b1e9-a5ed8da8c58e | -2.931 | -53.93555 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea35e790-4ded-38e7-902b-cc91c56d8e9a | -3.03485 | -54.10305 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb1ea4a8-c0b0-3ed9-882b-aaa3a837616e | -8.53803 | -66.98002 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66bcd6cd-866b-3b4e-9d9e-b4e0cbdf7cad | -5.29565 | -60.10415 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee8852f-1445-38ba-b437-771661e9cfac | -3.57502 | -54.35578 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99cd978d-b4a0-3f42-8d55-0c89b4bcedb4 | -7.21412 | -55.17041 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 283e2331-46b3-3e7f-b030-f831157544aa | -2.96607 | -57.76219 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bfc4d86-16e5-3ec5-b98d-b68594783769 | -1.19652 | -54.21167 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d78475bf-eccd-3aea-8a0e-c8b8b356cf28 | -3.01672 | -54.1042 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c81742bf-8c84-3bd2-8ea2-8e43a1c52b43 | -3.29178 | -54.07327 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dbb3e75-ce06-3420-afbf-d8d714e93381 | -4.42837 | -55.16468 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf331bfe-a148-315e-b0f2-6ab9afde7c22 | -4.45106 | -54.9762 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c62b565-7b02-37c1-9fb0-89733f2ce90d | -3.20917 | -53.86377 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45cf946f-a097-34cb-826f-02b63c713cc0 | -2.17039 | -54.45716 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a4120c5-5cfd-317c-b60e-0be95a233d20 | -3.29194 | -54.04934 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54425f80-e806-35f7-b570-08a1ca762029 | -9.48386 | -64.35809 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e781b27-d5e6-3544-afe0-3aee9d69e86e | -1.44486 | -53.23499 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33a3729-6cf7-31cf-a44c-e2f2d1ba7050 | -6.03859 | -51.72643 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5684f0-f954-3369-92fe-fa78d71143a6 | -1.34013 | -55.4628 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0af5dc7a-44f9-327a-b66d-8fe2b0785a59 | -4.06853 | -59.84874 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ae01488-55c3-3ec6-bb30-0433e0236c9d | -8.61956 | -67.00304 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b36e6af-aea9-3f98-8d62-bc6b34298a9c | -3.67385 | -54.50677 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 064a13b5-f065-3a57-a7ac-930647a99787 | -13.16685 | -54.3221 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 859c4cf8-1016-39e0-9095-b4fd84687851 | -2.86679 | -54.16087 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ea33e0a-62ff-3eae-8c12-a403c17d6959 | -3.22375 | -53.88653 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f409b00-15b8-35a2-8c02-06d6a0b0aa78 | -3.89606 | -59.44296 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8066ad-9a61-3939-aecb-1a3a3ba8e5e8 | -3.49803 | -59.2727 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbfc15f9-603b-343f-891f-14f97339c484 | -3.70765 | -59.6558 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d99674c-a6a4-38cb-b0da-40d588058a1f | -1.77456 | -55.06267 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45f5671d-afd8-356b-a501-37bc4369c1f4 | -3.58157 | -54.66579 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 439e9c1a-db14-3dc4-a9a5-a01ac4b4b076 | -3.30712 | -54.70452 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5386b8e7-aff3-34c2-99b5-17b449356645 | -3.10987 | -54.15295 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cd7a50d-4e80-3552-838c-cd3123534c74 | -6.1368 | -47.9258 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5c9b45df-e668-38c5-81f6-071c7bb53dc8 | -5.88461 | -55.55745 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05771ba6-f050-3bcf-8fe9-47d963244954 | -1.52558 | -54.53569 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c342692d-ae63-3869-9ea0-1aeca7076ba0 | -4.07206 | -51.03603 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36a89ac6-b2ed-3b91-9d64-e738f518510a | -3.17245 | -58.63005 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bf88d488-86d5-3354-9196-513742b5e47e | -3.32846 | -58.15849 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78d94c9d-b66e-389e-b347-5cfe70a5944b | -2.57409 | -56.16779 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4814edf6-259a-3214-bd7e-b68bf84cdc26 | -3.84488 | -55.98684 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bf5f886-2b46-30ec-aaca-0dca91b59be8 | -3.4823 | -55.43258 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c911b8-8cc3-333b-b722-89bd56d70f39 | -1.5068 | -54.80996 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba72383-2e6c-3b79-b08f-4ca98ff0b52b | -9.04503 | -65.92967 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c0bb7b-92f1-376c-904e-f7cc4b17fc6f | -3.2933 | -61.01696 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e70932b-4d8d-3909-aa1e-bf899b50f1fc | -4.45567 | -47.92121 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 871dc891-0f5f-325c-bbed-bfccc09e5cbe | -4.95229 | -55.11538 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfceeb32-314d-361a-8fe2-d5ae7f43c04f | -3.74819 | -59.31133 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d4213d3-57ba-36af-bcc9-49e6a150491d | -2.87961 | -54.1973 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c31245fb-5fbb-3eee-9a62-8dc667ffb943 | -2.78741 | -51.68212 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35f3a8f9-0dd8-3fa3-aed8-192daae5cf13 | -4.37048 | -54.75402 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97d35d00-e189-3931-a744-2ecdab5d9499 | -2.90359 | -54.01934 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8214f90-47db-32ff-818f-e94559c3f01f | -3.29239 | -54.06938 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea4ed20f-b2de-343a-89dd-00917f4bfb6f | -5.29858 | -60.10888 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce03656e-d550-35af-b372-56c07617c40c | -2.99003 | -54.06454 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b0c656e-d056-3198-9719-d4c3b4a200f0 | -3.07802 | -54.26614 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7ae7002-90cc-3fc0-a59d-a851aa27958b | -3.68981 | -60.5606 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69f69da2-97b8-3647-8270-47b791efe5b8 | -3.51116 | -59.21407 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2803198-6922-3089-98b9-ff872011751e | -6.95173 | -45.27623 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29fbad14-701c-3ac7-812d-da8aa575b5ce | -5.70901 | -53.49993 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05165657-d3a2-32c7-ac9d-37040aaadcad | -3.53775 | -59.48015 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c73a9709-a67b-33f2-921b-b801df0b11c3 | -7.21367 | -55.12692 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83064620-bea9-3c5f-b5ae-e8a4a840ae46 | -2.47299 | -56.10252 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08f1f3f5-588a-3381-aad8-f89b29344a59 | -3.80183 | -55.70355 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1236d163-7a61-3e2e-9098-cd953b2326ac | -2.96213 | -54.21775 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd25fce5-51f8-3aab-9c3a-de79d22c376f | -5.69177 | -53.48799 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c74d67fc-2634-388e-8f50-4a4617bf2f43 | -6.15263 | -52.64329 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf7162b8-028b-34e2-8f9c-676fa8125688 | -2.4718 | -56.06689 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea4f8c69-f145-37f1-86ee-fe9c40ebdc8d | -3.5442 | -54.67915 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2625025e-a706-31df-82fb-b8133037bb30 | -4.10943 | -55.17157 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a00ef0a-130c-3e0e-ad3c-57bfa5075720 | -3.11276 | -54.15741 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e25b0828-8f1c-38ee-8cf4-735570136e7a | -1.7219 | -55.44031 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 275d0b39-29b7-30b7-b699-48eb709cb63c | -3.18958 | -50.56453 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27c081f9-14db-348c-8c11-8eb64bb8b042 | -7.38537 | -55.18322 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 840e75c4-9656-394c-93f5-a74a266738fe | -3.5821 | -54.68501 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2503bbb5-e7ed-3648-8192-36e5b4ca90a1 | -2.49897 | -56.0676 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 728e47bc-abfc-3212-a475-bc9e0e8067d4 | -3.01863 | -54.06882 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23a28fbb-9d86-30ac-b624-84db4fe85668 | -3.60771 | -54.56623 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4f1f1aa-ad97-31ce-ae0d-55b5dd1ba7d3 | -2.93375 | -54.07963 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| daa385fb-81b6-3d1f-9cb2-951eadd77f2e | -2.83889 | -57.48384 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0996ab59-0e48-35e8-a4ab-5344f1ceca3b | -3.29547 | -54.04987 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0183089-6cce-3d9b-93dd-9d6cab893922 | -3.26146 | -54.03661 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2177fc81-0d10-3f42-af29-2d7485ca9ee3 | -3.01271 | -54.08378 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b9d48d6b-a440-33cc-a21a-f873c785e2bc | -3.9067 | -55.88877 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9a97c0c-e325-319c-a7e1-84ed5b96ae8d | -3.63506 | -58.9389 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93ffdc5-4d2f-3b44-8219-35437a09966c | -7.19815 | -45.34953 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e74bb238-6e88-3503-8355-fadd00c0be7e | -2.89049 | -54.08084 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 719409e3-a61f-3a55-848c-7fd0c5355a80 | -8.85099 | -66.80473 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 2111d9e4-8ee3-3d1d-9ca0-e8ba990200fa | -3.28752 | -54.00854 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README164.md)
