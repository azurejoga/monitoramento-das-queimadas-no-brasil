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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e66da32c-36b2-3976-a735-9a43e127d97f | -3.1097 | -54.2865 | 2024-10-29 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 94893ba5-1d25-330c-ad9a-2018fdcd3d3f | -3.1794 | -50.3922 | 2024-10-29 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d9fc6c04-8ada-3a53-8682-3d3d750ee869 | -3.2503 | -46.8709 | 2024-10-29 05:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e611c5aa-c29f-3fbe-9712-7cffa8f7bb6c | -3.9289 | -48.3458 | 2024-10-29 05:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5eb0c872-b5ae-3dd9-914a-8ecc7d631572 | -6.1182 | -42.5086 | 2024-10-29 05:05:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 63a291f7-913e-34cb-81ef-9f2114e8be31 | -6.137 | -42.507 | 2024-10-29 05:05:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 153d739e-fb8d-3cc4-ad1d-34ee9f28ee15 | -14.59156 | -44.26185 | 2024-10-29 05:06:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ceadb3e-d5be-3cb2-899c-47af03fa6653 | -13.2558 | -53.9258 | 2024-10-29 05:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd3f167-8e2c-3b56-acaf-b0ac16280d92 | -13.25215 | -53.92524 | 2024-10-29 05:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e242dc5-66fb-3449-bf13-8e31c0cb0e2c | -12.79007 | -57.01968 | 2024-10-29 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a40bfe-49c6-3dcd-ab31-9b295feb2cfe | -12.7801 | -57.03982 | 2024-10-29 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3967e61b-0337-3fc8-b7d4-656d772f30dc | -12.7601 | -56.64825 | 2024-10-29 05:06:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24535ac3-8b38-33c6-ac52-9e74e6e102ef | -12.75954 | -56.65181 | 2024-10-29 05:06:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d37fa469-2281-318b-a278-31682e4964cd | -17.79561 | -57.36842 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2cb5a509-57b0-30a3-9c70-e0f16ba41c0b | -17.79505 | -57.37211 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2184412d-509d-3063-81cf-1ec83d0096e5 | -17.79449 | -57.3758 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e3c8e9bd-be13-37d0-adda-dcfd5b1dba9f | -17.79226 | -57.36786 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6c43f7dc-f2a4-3c81-8113-6374da59eaff | -17.79169 | -57.37156 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 42b6cae8-b258-32fb-8873-83bdb14f2b10 | -17.79114 | -57.37524 | 2024-10-29 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aba00c0c-ca2b-3dca-8950-f776ed343ef1 | -12.42776 | -57.8737 | 2024-10-29 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd8d12e3-5611-3227-af28-6b7592e83546 | -12.30478 | -58.15604 | 2024-10-29 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82ba8682-84d5-3345-8a1b-9843444e40a7 | -12.30142 | -58.15548 | 2024-10-29 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ae86d4e-246f-3b73-9054-64b6953a6df0 | -12.53392 | -63.24893 | 2024-10-29 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa930f86-04c8-3b99-9617-8d5d586dca33 | -12.3334 | -49.9208 | 2024-10-29 05:06:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8fa76397-ba73-309d-a991-439f4464ff7f | -12.3522 | -49.94 | 2024-10-29 05:06:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| dff4523c-c1bb-3bd9-bdf4-db38bf556b04 | -12.3526 | -49.9184 | 2024-10-29 05:06:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 676b355e-073e-3daf-95f7-7a2f3a3513fe | -19.61612 | -56.69581 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 914885ef-aa96-3e70-8957-ec94192161c8 | -24.24423 | -50.73845 | 2024-10-29 05:08:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e175875e-bfa6-3736-a9b9-c62d3ae9a569 | -26.59504 | -51.74987 | 2024-10-29 05:08:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5208c4b8-3ba8-38e4-8368-05310879a87e | -26.59499 | -51.74971 | 2024-10-29 05:08:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b3c65727-7bd0-3d9b-9d0e-93979fce4313 | -23.9987 | -54.12075 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0f4f6194-eff6-384a-a8d0-33dbd936ed1f | -23.99821 | -54.12476 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d48e4344-4a8c-3423-b232-ed51cb1be783 | -24.8712 | -53.47789 | 2024-10-29 05:08:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3e35b6ee-f64d-30f2-a7a5-d0e1a96fb12e | -21.804 | -53.49129 | 2024-10-29 05:08:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91a951ad-317e-3262-84c2-9b489fc931fd | -21.8035 | -53.49537 | 2024-10-29 05:08:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c655c835-0bc3-35d8-a6d9-3a8ded6c6979 | -22.96073 | -54.9015 | 2024-10-29 05:08:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a52f2813-ef3a-3b33-899d-43139a940d2c | -24.01062 | -54.12652 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 51a790c8-c604-3d4e-91c7-250584a3a3ca | -24.00698 | -54.12191 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4039f964-ee1c-3589-85fe-b220646f4354 | -24.00648 | -54.12593 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 55afb8c2-4cf2-3653-b11a-e91b956b9933 | -24.00284 | -54.12133 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7eb36097-d723-3143-ae20-5340a15348a1 | -24.00235 | -54.12534 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b63a253f-356c-3011-886f-e4c6f6da18e5 | -23.99919 | -54.11673 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f9bdee2f-9535-3fe1-bb8a-6ffc410c878e | -23.99505 | -54.11615 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b283d282-fabd-37b8-a7c3-0415a4767930 | -23.99456 | -54.12016 | 2024-10-29 05:08:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| da0e1dc2-f12e-3579-9d27-80cf4b0927ec | -19.61152 | -56.70317 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eec96f94-9e2c-315b-a212-82f615b0a368 | -19.60117 | -56.7015 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 35df032f-b2fc-3743-b5f1-a9ee601d0aa7 | -19.59829 | -56.69697 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a36600c4-e192-34e0-80f4-87c9676c70d9 | -19.59772 | -56.70093 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cdd77e60-fa5d-31e3-9143-6f047a75b4c3 | -19.59715 | -56.70489 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 34a6b1d8-d8aa-39ee-8f97-59dfab3eca28 | -19.58786 | -56.70804 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f20fbfd-9512-3664-b410-9b3dd0af4d0e | -19.58441 | -56.70748 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d5550ac9-94c6-3e2b-a188-5c55405d70fd | -19.58383 | -56.71143 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a272690b-7209-3ca4-987c-0877742002bc | -19.58096 | -56.70692 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0bbff06d-bdf4-3a51-afb6-b4297f706145 | -19.58038 | -56.71087 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 34b378c6-b6b7-3a67-a9d4-e4143c6d7165 | -19.57693 | -56.71031 | 2024-10-29 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 12409160-c509-385d-ae20-34befe683c72 | -19.50958 | -56.58979 | 2024-10-29 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3d288136-ea93-3aae-8f2d-667ce7661bcf | -19.50901 | -56.59377 | 2024-10-29 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ebe23221-9a19-3b6e-8e01-35f1f568a540 | -19.50554 | -56.59322 | 2024-10-29 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1d484864-0e33-3e4f-883b-481797bf427c | -22.08821 | -57.97662 | 2024-10-29 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 15e172c4-150b-3b17-bac7-f37ef68c4c81 | -2.8145 | -49.2418 | 2024-10-29 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1a36e13c-5e29-3a9a-9f9c-b51219f7c6e5 | -2.833 | -49.2413 | 2024-10-29 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 600e60a1-40c6-35fc-9756-c086f4a7af7e | -3.1097 | -54.2865 | 2024-10-29 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e522fe18-1109-3a92-8258-93136fc805aa | -3.1794 | -50.3922 | 2024-10-29 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 79ef6585-c638-3f46-93dc-eec084e73e84 | -3.2503 | -46.8709 | 2024-10-29 05:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e6b8c2a4-cb42-38a2-a13e-35c341fb1237 | -3.9289 | -48.3458 | 2024-10-29 05:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5e496469-6a00-3dac-83c2-f92c9f11d175 | -12.3334 | -49.9208 | 2024-10-29 05:16:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1268afd0-b201-3428-8768-8dede8708427 | -12.3522 | -49.94 | 2024-10-29 05:16:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 35ea44d9-99b4-355d-b54d-8d768d9da1e0 | -12.3526 | -49.9184 | 2024-10-29 05:16:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d14e8c95-2e90-3a8f-b59a-1e518ae3fefb | 3.58772 | -51.26785 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e863a22d-baa1-3a37-a804-6d5b56dd5a95 | 3.58104 | -51.29107 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0481eb3e-14a0-31e1-b86d-e4a52a6330ea | 3.58053 | -51.288 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 079d9bb4-1056-3a3b-9178-38a44c92cae6 | 3.57384 | -51.27963 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58ea4636-054e-3870-b17d-4f6ffcb0c80b | 3.57332 | -51.27656 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2698189-06cd-3082-b53b-df4970771e93 | 3.5728 | -51.27349 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41f27aba-f597-3d84-b079-81c960a4eff0 | 3.56973 | -51.28664 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a41d91f9-de29-328a-bb22-4d954db22d6e | 3.56921 | -51.28356 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30a2f0b8-551e-34a1-bd34-e9bf4b879095 | 3.5687 | -51.28048 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f825390-2d68-35e8-9ddc-cf7863099328 | 3.46484 | -51.24217 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1030a9-f12e-36f9-8ba7-fba0ba9739f4 | 3.45968 | -51.24303 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06c4c99b-10fb-396b-bad2-4ce7191bdca7 | 3.45504 | -51.24698 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4fe8b7c-b103-31ab-b46e-1ca9c818dd4e | 3.4525 | -51.26336 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e034bd5-c377-38f8-bb6d-beaf3d2ecafe | 3.45145 | -51.25715 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4182d3a3-4e5e-33e1-a89d-0d66528154e8 | 3.45092 | -51.25404 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ad58c50-4b3f-302a-abc1-1d5d34312369 | 3.4504 | -51.25093 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df45ceff-f60f-3c71-8011-1ab8cce5ea15 | 3.44734 | -51.2642 | 2024-10-29 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77d603b4-f04e-39e3-b840-51db80b61d6a | -3.63785 | -54.67924 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08a06bea-bb18-3ea2-9e92-1cc6ca162b85 | -3.66005 | -54.37051 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8a892a9-aba7-30e0-8bd7-c75bbcc631e4 | -3.65537 | -54.36994 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 082d4b6b-5d50-3c84-8589-df5e87e21f59 | -3.69446 | -54.07025 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2104f4d0-9070-36e3-ac8c-7a832849b52f | 1.60177 | -55.63475 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 062cc11d-f3f0-3471-ab30-91a6bbf64e54 | 1.58833 | -55.6265 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c515ba42-cbe4-34ea-a38c-ac3a131468d7 | 1.56941 | -55.63468 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53c8a7cd-840a-3280-8016-469d571178aa | -1.2133 | -55.86192 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a48bb3d6-6413-35b5-b8ca-9bd7f5b7bdce | -1.21274 | -55.86547 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c66daef-a30d-3563-813a-ea50569c2165 | -1.21064 | -55.90527 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f6c6404-3b0f-30a6-8645-a2da7ae73fc3 | -1.20866 | -55.86501 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de64a2dc-ea20-3761-aaea-a44f901ee78d | -1.2077 | -55.89764 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4be28e0b-bfc7-3ef0-b4de-f4e837ac3ea9 | -1.20754 | -55.8722 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c885e48-4e98-3718-846e-08fd6984b775 | -1.20713 | -55.90126 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d50040c0-5287-31b8-b530-0fd2e87780a1 | -1.20699 | -55.87566 | 2024-10-29 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README95.md)
