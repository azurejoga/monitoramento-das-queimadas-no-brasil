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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c63fad77-48a8-3857-9703-338b1523cf12 | -16.88764 | -54.1412 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 9f9f8e0b-4e20-3223-8102-341bbb1f272f | -16.90416 | -54.16217 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c728b9db-08e6-35a1-af9f-5ffb7bbe3d10 | -13.42772 | -57.05984 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e3609549-0931-3523-91e9-f2fccdae071f | -14.31019 | -53.09613 | 2026-08-15 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d6494a9b-a117-3180-8ab8-4f816aac9946 | -13.23552 | -54.16608 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d7a28fef-227b-38a0-8e06-e3aaa965e518 | -14.74841 | -56.35398 | 2026-08-15 00:50:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8aa700ef-43b1-318a-a5e1-defd490bd30c | -14.44825 | -51.96032 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 25db736c-7b53-3e49-9a7c-5956a684a08e | -11.48831 | -54.61998 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 02b14955-3307-31da-94f6-0053085c966f | -14.46835 | -51.95089 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 793dcb11-55d0-32ff-8f72-2637a306725a | -14.13329 | -53.67572 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bba5a517-25d1-373f-93f7-e52629e7d710 | -14.31104 | -53.09033 | 2026-08-15 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 61620536-7d82-3ad6-a49a-2e9aea22596f | -14.12855 | -53.6832 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 53427b43-6c09-3a2d-90f4-dbe364b0b4ed | -14.06572 | -53.67699 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| fb6c87de-fffb-34d3-8215-c90b6efa5bb7 | -14.43049 | -51.93912 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2588d92b-e5c5-3922-8d7a-179166037e9f | -11.5026 | -54.63445 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 45a7f381-3c5f-363b-b245-b90a04f63757 | -16.87973 | -54.15119 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1b673134-49db-30fd-8f9a-cdf38602fbbb | -14.44008 | -51.91273 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 392cae57-58b8-3a2c-944e-ba16c11c758a | -11.59009 | -54.68099 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b8cf00bf-6a23-3098-92ff-8f016da36752 | -14.10749 | -53.70572 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 395155a8-3bae-3428-81a3-b719ea83c590 | -11.51215 | -54.64318 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8e3ff321-fa23-3095-a8df-b567cd274da7 | -14.42488 | -56.25648 | 2026-08-15 00:50:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 70da0284-401f-3934-9d29-51aaef2ed4e3 | -14.08348 | -53.70979 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 1e8d8c49-8e3c-336e-9e81-d50db47aed1a | -13.23824 | -54.18294 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9956fde8-c860-3265-a7b4-fdb7cb394c69 | -13.42614 | -57.04914 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3a98472f-9b68-3bff-b17b-a376519f6c8d | -16.8774 | -54.13717 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b64ba537-6232-358c-b5ec-27b79a4c4939 | -16.89076 | -54.14949 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 242d82ae-7bfd-3766-9640-aa0ee93f6d74 | -14.45786 | -51.934 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5140bbf5-5e78-3ccd-96be-1af8cbd5dcb7 | -14.46191 | -51.95774 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7afba6aa-f969-3bac-8b78-705838189128 | -11.50948 | -54.62675 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 937b82b6-6da8-38ee-933a-2a8b43741295 | -14.45378 | -51.91013 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 2963206b-ff1b-3a52-a4b5-c100fd14b352 | -13.76054 | -53.42804 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0e91083f-0b7b-3975-b091-e45be3e0e631 | -11.50002 | -54.61791 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2d23cac0-dc38-3ed6-92d5-08bd795a08ed | -13.2527 | -54.19784 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 77ac6180-5c6b-32e7-a14d-b6009284f9ec | -14.09584 | -53.63393 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1066ad6a-8fda-32c2-b09e-5941d901e04b | -14.42637 | -51.91528 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| dbfea32c-c1b4-37d3-aa01-94aea3d5136d | -6.96896 | -59.28012 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9a83c4a1-7874-37a3-9c71-45efc21a11a0 | -6.95271 | -59.28842 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f408814d-5caa-39d6-b671-01b9c29d54e9 | -6.95981 | -59.28146 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| e0ae1f74-c86a-3fdc-b140-4ee02f658abc | -6.96255 | -59.30061 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4c4a3e92-f6ec-3fef-941a-b7872b6ec2b9 | -6.93985 | -62.88213 | 2026-08-15 00:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 0f54b7b6-207c-33d0-85ae-80779e141668 | -6.60715 | -58.99873 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| c46558f5-5624-3fe0-9755-91ff919489a3 | -6.61832 | -59.07777 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 5fc1be71-50a4-3e56-a711-0170755a4c50 | -6.8505 | -58.96484 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e7c7e996-d00d-38f1-8b5d-c4c483e25df1 | -6.80443 | -58.77736 | 2026-08-15 00:52:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bec84521-7aaa-310d-baa8-8ab45abdc3f3 | -6.59924 | -59.00999 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b9dde006-0ed0-354e-81a6-9610a95d8cf4 | -3.51945 | -58.95173 | 2026-08-15 00:52:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 918a6fd0-ad36-3ed2-8af6-e4e4165748e4 | -6.20502 | -57.76073 | 2026-08-15 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9c9bc1b1-ca16-3b90-807f-a8db73d2beb7 | -6.59783 | -59.00006 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| dfb537f6-649c-36c9-8edb-a8cfa3a59261 | -6.61693 | -59.06791 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| ddb5d784-3c7c-355f-9ee1-a8704802c305 | -6.54106 | -55.17985 | 2026-08-15 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ab52ad2e-efc4-3cac-b64f-6d740d814cd8 | -6.58271 | -56.35302 | 2026-08-15 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 038b7abb-2996-3df9-86a8-731d48ec4c80 | -6.7844 | -58.74487 | 2026-08-15 00:52:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 956829e1-4377-309e-ab64-19e7fb2225d1 | -6.02146 | -57.83662 | 2026-08-15 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7e41f6e0-1ad5-321e-923a-879ceeadb042 | -6.93855 | -62.87248 | 2026-08-15 00:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 84b15473-e957-352e-ae79-0a8ae398ee97 | -6.69382 | -58.95942 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 826064f1-5e80-3b86-8555-6a0705b38e46 | -6.9717 | -59.29928 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7e32ab21-e3fb-3ca6-83cd-adadefd0c270 | -6.20676 | -57.77255 | 2026-08-15 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8ad0641e-1ca0-3499-8f21-0940d123097e | -6.61415 | -59.04826 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6350db5e-e494-3369-ba41-cd0ef680cb53 | -6.71898 | -58.93528 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c13634d6-1524-36b7-8e8b-6efd214c5b1b | -6.72038 | -58.94525 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ac10064-f563-3cc5-8cca-74a0231dd3e0 | -6.97034 | -59.28973 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9b601329-9c2f-35cd-855f-8f462419b79e | -6.62482 | -59.0567 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9b111dcd-ed7b-3976-8c4f-7ba612949113 | -6.65643 | -59.096 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 193246dc-60ac-3267-aa85-352a2bc25d26 | -6.61971 | -59.0876 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 80b0d0d0-1104-3309-a06e-34560819026b | -3.59603 | -58.63155 | 2026-08-15 00:52:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4661e843-2e6d-3c11-a62a-ce248fe07c95 | -6.53822 | -55.18581 | 2026-08-15 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c585816c-bd73-37a5-a8aa-59631a8f85b9 | -6.71106 | -58.94662 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c293b1ab-7e63-37b5-9849-e65a469a27c4 | -3.59443 | -58.62028 | 2026-08-15 00:52:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ad8806e1-7862-3248-9b6d-2b20266f6d47 | -6.62621 | -59.06656 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d29ce310-ca2e-310f-b9fc-09596d5d5f97 | -6.58492 | -56.36792 | 2026-08-15 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cd771f75-a24a-3dfc-89ad-b5eab328e4b1 | -3.23949 | -61.16526 | 2026-08-15 00:52:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4bcfc645-1b20-3551-a218-d73c1293483b | -6.65029 | -59.10333 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 006aeef9-0565-31b6-89a4-84c30f7a92cf | -6.61554 | -59.05806 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 168fd602-e9af-33a0-a565-e650759d5e38 | -6.61646 | -58.9974 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ea9f1758-c86e-369e-aa6b-8b162a9d995b | -6.01975 | -57.825 | 2026-08-15 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 507cdea5-65c1-3263-b46a-f00c91c01f25 | -6.8868 | -59.02005 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a5e10d5a-91ac-3f68-a018-87a0f3312591 | -6.96118 | -59.29104 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fc623043-f22a-385f-ba0e-c768388d370a | -6.70175 | -58.94812 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 3a3c8747-fe2b-3014-a810-e030eca60a5c | -6.8598 | -58.96349 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 34910923-f5a0-3914-8a39-1bb75a5c6f9f | -3.73928 | -59.33554 | 2026-08-15 00:52:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a91d844b-43b1-335a-a793-4b43c3f2a43d | -6.95405 | -59.29801 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 253.9 |
| 40da5d29-32a3-328e-bbfc-1d1e9a69b15e | -6.62344 | -59.04687 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a25f0911-f59d-3922-b052-43ee51d257ca | -6.69242 | -58.94952 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5edd103f-53e3-3071-b90f-288ae95e7750 | -6.80295 | -58.7671 | 2026-08-15 00:52:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 06aed899-1a9e-33d1-98ac-39a595c00791 | -6.60855 | -59.00863 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7d4c641-8e31-3197-8d8c-ce0ae84c9d7c | -6.94491 | -59.29938 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4e1762da-7de3-372f-9cd5-3a169d19aea9 | -6.71759 | -58.92529 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d45d8f5-4247-365c-a4bd-a9ca7b894b63 | -6.70315 | -58.95805 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f6cea393-a27f-30a0-a060-ed1a1ab86a39 | -6.65786 | -59.10589 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 55b69559-8416-3914-8d29-234cc0498504 | -6.61506 | -58.98745 | 2026-08-15 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38bddb49-0697-3773-8697-801c0d33a659 | 0.89104 | -59.69768 | 2026-08-15 00:54:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d258958-847f-3031-870a-616f88300d43 | -14.4499 | -51.9004 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 19eec664-9c31-39b1-a5df-3a1a4c47d06e | -3.9785 | -49.4563 | 2026-08-15 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7b8a7a79-fa13-3034-a928-a53c4faff921 | -6.9145 | -43.6351 | 2026-08-15 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 688be589-acbf-33cf-baa4-4c380f005cd6 | -14.4495 | -51.9217 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 936e7f81-7515-3985-a291-106a5b5a7acb | -6.6197 | -59.003 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5af95981-097c-3c94-aaad-a3966c826193 | -9.1219 | -46.404 | 2026-08-15 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 47ba78f6-f881-3483-9a32-55d1ddb4f21a | -14.4488 | -51.9644 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f29cdad1-5b8e-3662-a19a-092572073682 | -6.95 | -59.2984 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 30a4fb11-4a0e-3c06-b916-fc31219dabcd | -14.4492 | -51.9431 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |


[Clique aqui para ver as próximas entradas](README4.md)
