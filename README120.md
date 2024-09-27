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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca56ba83-668b-3fa7-bf09-8cc4811ba43d | -7.49144 | -60.71781 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eff348f-e819-375f-81ba-3932e41dc1aa | -7.49088 | -60.72143 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d271e703-d8bb-3d2e-9cf4-6c266348d535 | -7.48908 | -60.66536 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c650ade-e16b-3439-896c-a971ed3fc0f7 | -7.4875 | -60.72091 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97472ee9-035e-3819-a6e3-90d1bb595fea | -7.43815 | -60.62779 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba3203b6-217e-3c77-aad3-461626e36e62 | -7.43476 | -60.62727 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b32e177e-3a3f-3841-b5ff-e1b90f19379a | -7.43194 | -60.62312 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd0c9b54-edb8-30c2-b409-09746f36b7a6 | -7.24334 | -60.71691 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ec55557-2a9a-3b82-9cff-24bc388fb78b | -7.2097 | -60.67844 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6e9d194-264a-3669-bfa6-6f22c6fd4e58 | -7.20914 | -60.68203 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dd4df15-a702-32ab-a795-5b0530e9a838 | -7.20744 | -60.67065 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8afd0a48-196f-3f8f-8871-248df8240d87 | -7.20462 | -60.66652 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec35286c-c5ef-3914-894c-892ae46bb763 | -7.20237 | -60.65872 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 703a4d75-a0ce-3a9f-a86a-61e330fa6552 | -7.20184 | -60.68459 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef2c5367-73c7-37c2-8e79-fdd5bc30529c | -7.2018 | -60.66237 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f802c1c-e967-3630-a38e-04d1c50f81cb | -7.20128 | -60.68821 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b2df565-2c40-3419-bdf3-5d6bd49a9d87 | -7.199 | -60.65816 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77ff0526-4147-3bd0-9ae7-30c0cffe71f9 | -7.19846 | -60.68409 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3dfa43b-edef-3cac-b4a6-26d5af519599 | -7.19843 | -60.6618 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ce8d08-e7ef-38e4-841c-afeb78af3468 | -7.1979 | -60.68771 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f1a831c-ffd1-34a3-a300-3b195f6c19e5 | -7.19564 | -60.67997 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c0bb70-23de-35fa-967e-1043f5c39fb5 | -7.19508 | -60.68358 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaeec447-bb96-3943-b211-ba9852f27d68 | -7.19452 | -60.68721 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10e61f1c-b664-3cdd-804f-8adc825dedf0 | -7.1917 | -60.68306 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1793949d-b693-3f62-bac0-b1b2215b88b3 | -7.16693 | -60.6643 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4c8d997-243b-3a47-a9ae-ed3c6e83ac63 | -7.00649 | -60.67736 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b53d398d-1eb0-3693-84c0-8d4c810a8735 | -7.00312 | -60.67684 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180460cf-0924-3c53-8bcd-dd973fefafe4 | -6.98675 | -60.62632 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 517b424d-98dd-3dcb-b53f-a9d31bd59e61 | -7.4892 | -60.06589 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b5885ec-efbd-3ee9-96ad-c95327b9932e | -7.4692 | -60.4036 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7758e9a3-3176-3c54-88af-4d2f91ca556f | -7.46919 | -60.42635 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca953b22-5320-37f0-a632-dc552ecef960 | -7.46862 | -60.40734 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11858b2a-3fbe-301b-b3f4-4dceeaeaf053 | -7.46692 | -60.39573 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbb9b47f-3ffb-3b0b-b211-1fb98aaf02d3 | -7.46635 | -60.3994 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5749e684-9700-3c75-87aa-ce7f805ea1da | -7.46579 | -60.40309 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64461b95-f440-3f80-8b88-18762d1a76df | -7.46521 | -60.40683 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5028cfac-c0ad-3f5f-bd15-4dc4e4efafaa | -7.4635 | -60.39522 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d57fc117-d084-350c-a8e4-5e97f42027c1 | -7.46294 | -60.39891 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b678ba-93c3-344d-9651-fde99568c74c | -7.46237 | -60.40259 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2216113c-df03-38dc-9418-36092ee75819 | -7.4618 | -60.40631 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 796350a9-e870-3727-98bf-bcb753c906cf | -7.46122 | -60.41007 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d54c69a-7a1a-3f8c-8244-5c5aa19e51a9 | -7.45953 | -60.39839 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c759cb9-8ab2-3835-b845-73828ca4c199 | -7.45896 | -60.4021 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ec3f34f-2fa6-3df8-b8cf-a127405f3892 | -7.45781 | -60.40955 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c57ab49-2f3a-38d6-b70b-1b16ef24e349 | -7.45725 | -60.41325 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b3d8d63-1b68-3dc2-b305-0c81cbb08bcf | -7.4544 | -60.40902 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 731c0095-b54f-37df-966b-c28b6c0ac988 | -7.45384 | -60.4127 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f2079e-4dc3-3e1b-bacd-21be28376e1f | -7.45222 | -60.51398 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4f1ffb-141c-39a9-83f0-66cdb1a91a91 | -7.451 | -60.40846 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d70aa5a-aa13-348c-947f-6de07aeee56e | -7.45044 | -60.41216 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1a45430-90d6-3f38-8628-fa00454159f3 | -7.44947 | -59.77773 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b521ce95-5fac-38eb-a6b7-0a99539a394e | -7.44598 | -59.77722 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3bf9410-24bc-3729-baed-6e0503643dee | -7.44478 | -60.42632 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d054d17-0f12-323d-bef9-1f3b08c26200 | -7.43239 | -60.50718 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2842dea-5469-3ab9-b91c-76277e3c70ad | -7.42899 | -60.50666 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66f6de4-4199-3b20-b5ac-bf1051930430 | -7.4058 | -59.80689 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e98450-89de-312f-a992-73e512ecf937 | -7.40522 | -59.81076 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ffda485-c9f6-30d6-a1ae-3d0a1f71a757 | -7.40057 | -59.79427 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ba442ab-6461-3c1c-9a0e-36d2377ca997 | -7.39705 | -60.41916 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 834ce8b1-9030-3acd-abf2-1bb9dcd78cc5 | -7.37156 | -59.86898 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9add9ea-624a-32d5-80ae-a9b8fe4ed6e0 | -9.35315 | -59.68384 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6dfd3b0-c6c2-3d2b-9b71-d6d1c7bd360a | -9.35254 | -59.68798 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfc5198c-806c-3ae5-92dc-6c5d5af9168d | -9.34957 | -59.68336 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f53bc505-01ed-3684-be05-7d75f7b29857 | -9.56948 | -59.7852 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceeb0392-ec84-3dca-9ed8-246c65414187 | -9.56592 | -59.78466 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bdba76f9-5d61-3a6b-bba3-07b81fd49269 | -9.95352 | -60.24107 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ece4c72-3b92-3563-aa47-6eda4d932005 | -9.95118 | -60.23267 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2c90af-1f27-393f-bd8c-347a5c40aaaa | -9.9506 | -60.2366 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b20d422-e2b8-38a3-a244-5c3aad7f8a75 | -9.95001 | -60.24053 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31433bbc-7e05-38e9-9117-49cbe5ed9c0d | -9.94943 | -60.24446 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec18d5fa-9ecc-3c67-9e46-20e2da705e09 | -9.94767 | -60.23215 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ececde00-e4aa-321c-a572-e8c6d3d3eccd | -9.94709 | -60.23607 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3d3b30a-436e-31d8-a26b-58baa7f864e6 | -9.9465 | -60.24 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9ce0865-4e32-3fec-92ab-ab7e8dd13c6d | -9.94592 | -60.24393 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6d99791-a1c8-3a3f-95a6-a32cf2d4c1fa | -9.94416 | -60.23164 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac19f89e-1c8b-3d58-a020-ad09795afaf3 | -9.94358 | -60.23555 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76eba81e-ee1a-37a6-95af-1313a92e3729 | -9.943 | -60.23948 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 181665e2-e830-3c6d-8127-427494e284a6 | -9.88346 | -60.27132 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1749411a-f211-3892-be44-54be3a1f941c | -9.87996 | -60.27081 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8ca0b71-6464-3893-9482-b8334c23dbb8 | -9.82341 | -60.48072 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7f6a9ed-37a8-329f-b2c1-58612d240cbe | -9.82283 | -60.48455 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e30617fd-53f9-37ec-b3c4-6899328e9876 | -9.82052 | -60.47632 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4725cc1c-91e0-39bb-8fdb-aaed1980df43 | -9.81994 | -60.48018 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337a0185-3072-344c-a361-89fad6f39466 | -9.81937 | -60.48402 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cca9448-f7b7-34e2-8a68-545edc5f3bb8 | -9.81706 | -60.47579 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c85c7cd3-6038-384b-a13a-32c8956daf49 | -9.81648 | -60.47964 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f72247b6-fefd-3f7d-83bc-41b4a48903b9 | -9.81359 | -60.47527 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97cc0cbb-0ec1-312c-af89-be62a911cb16 | -9.81301 | -60.4791 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5224db05-e8b5-3791-be6b-ea9d6f9cdef3 | -9.41145 | -60.56912 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56e0578b-df32-3f83-8228-c404b81f9e23 | -10.70735 | -60.71622 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1440d74-1758-3cbd-9850-7e7f5dcb3ff5 | -10.70509 | -60.71624 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cfba2f1-612a-35f5-b762-bc78b2dba83e | -10.70451 | -60.7201 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aec6cfe-657b-330a-898b-49bce740cda8 | -10.70389 | -60.71569 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99c234b8-ad97-387a-8995-cbd2193bc0bf | -10.70332 | -60.71955 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60738243-81ee-3f45-b906-9f3a7b5051c1 | -10.70275 | -60.72342 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a2eba2-f9c7-3b4f-af52-7291ffef5b40 | -10.70105 | -60.71957 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98fc7d53-461b-3318-8c54-c9c675ee8433 | -10.70046 | -60.72342 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2abf80-d676-3b5f-888d-90ac6e4ac8e7 | -10.697 | -60.7229 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f19debf-e22b-3ac9-ba62-b8108a70a7a1 | -10.69642 | -60.72674 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcba78cc-9c39-3f44-8b5e-84d201fbe105 | -10.69237 | -60.73005 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README121.md)
