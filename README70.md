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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7e2d3af-9264-3002-b2d2-49ce924318d0 | -6.12403 | -57.82041 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e968a5e-cef8-395b-808a-25b2f607be01 | -6.74565 | -59.64112 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6de44bab-eef0-3712-a946-e11aa6205a60 | -7.51321 | -61.38135 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6bb30a09-d8db-3039-afa5-68f35c6b4a54 | -6.99095 | -59.27526 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f203624c-73ad-37c2-8b9d-bab37cdc554f | -7.02801 | -59.23523 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 103a2f38-30d4-30d3-8da7-a1842b553447 | -6.85816 | -59.41407 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abbd7cab-ba76-3f8a-847c-f7a73663877f | -6.14944 | -57.94886 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 254364ef-1dd7-3feb-b31a-1588468db04f | -6.64194 | -58.49574 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec657e56-2171-34db-9f8e-5ce54814c534 | -10.16527 | -55.3107 | 2026-08-26 05:48:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2799b53d-f49f-3565-a913-90c8a90123a5 | -7.77455 | -61.56983 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1980070-b815-3317-85f8-c58b47e8beee | -6.23032 | -55.61961 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49de2d60-88db-335d-aa45-54ce79011c74 | -7.01979 | -59.22951 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5885b69-e7dd-3f3f-920c-d52f835e6950 | -6.2713 | -53.37047 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 939f801c-394a-3cda-9413-3a255c22f8ae | -6.14763 | -59.929 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6de2833-67ee-394c-b1c3-0e777fa7794d | -6.62874 | -58.48896 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12e16a1a-9aa5-318c-a724-51361509aeee | -9.09469 | -59.4059 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| df20d56e-3010-36d9-a79b-7fdbb5518636 | -9.67544 | -55.08555 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98b041df-57d8-396c-a6b0-97936d2a51f5 | -6.93995 | -62.88254 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33a8105e-f8b7-3f82-9963-3f17f779da99 | -6.40465 | -60.05454 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c08b05bc-82ce-3949-a38d-19a4ffec8772 | -6.64587 | -58.50119 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4c2cc02e-7dea-3c01-b2ac-5d00dd89f9c4 | -7.51563 | -61.39162 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ba6b3756-6766-3de9-b43d-52eb12a61095 | -8.64477 | -54.75319 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1091849-512c-30e8-a455-2e2d1b8a8873 | -7.03182 | -59.2402 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ccd5ded-e230-3167-be80-a88bd1fdc307 | -6.12327 | -57.82254 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 787958a3-2cf9-3709-a122-445d61a52b69 | -6.98463 | -59.28751 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a358748c-4912-3990-8ca1-f29210756a14 | -7.31564 | -61.14777 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ee9d3e8-9dcb-3f03-b053-d657a8f9485d | -6.12807 | -57.82333 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67a839a9-c9fe-370e-8cd7-71e3e02cdef2 | -7.52022 | -61.38735 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 392188f4-c787-3dd1-a7c8-f74bba7f46d4 | -5.941 | -57.73667 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 827bf9eb-b49f-3c27-9c1d-9f1c90ecece0 | -6.9948 | -59.27889 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a312023-e741-3e98-b73b-ea3ebbc30bbc | -6.27777 | -53.3713 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21f0247b-b266-3a68-9f11-2a1d2bf601f3 | -9.27946 | -60.90057 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e4d2dd-f5ac-3aec-a22b-96870d5855be | -6.63062 | -58.50869 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 035960f2-393c-34ca-a136-092b2f8e36ff | -6.73594 | -62.98684 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d45234-1ccf-3763-bdce-a70d21a87c90 | -7.3922 | -55.15585 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 116ff1e0-c725-3871-a208-ce7e6bcb4fbc | -6.82056 | -58.65165 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b77afe-1791-36d9-b04f-92b4763ef550 | -7.377 | -55.18032 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e35de3c-87cc-3ac3-952e-fdb9dda9112f | -7.10988 | -56.56876 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79a31a7e-43f4-36a3-98b4-4864fe693fe5 | -5.77695 | -57.54835 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7304076f-2923-3ac5-ab1b-da3b353c87bc | -6.6544 | -58.5075 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| eb9d5715-56ff-3679-8af5-24693d4a67d4 | -7.4345 | -59.77595 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dc26250-d782-388a-9e85-e2ae5f476793 | -7.01855 | -59.23827 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0ea7805-2a7a-372d-9d44-8acc4c456ecd | -6.626 | -58.508 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d7d0e56-4a59-31b6-aa48-561704c9fd67 | -6.14719 | -59.92195 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 766110b4-16b7-30d5-bb07-072ff737b34d | -6.11773 | -57.82706 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 71fb1e40-4926-3769-af53-7dee8490254e | -9.97036 | -53.94857 | 2026-08-26 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0402d82-915e-30e3-83fb-fc878cee5463 | -8.64678 | -62.89328 | 2026-08-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c5408a-8c0d-3563-acb6-d2c168c9e09d | -6.80882 | -59.68749 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07919e4d-b7ac-3da2-bddc-f7dc44163aad | -6.63985 | -58.51011 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 412924c1-6ee0-3124-9909-794f79bd1e54 | -8.5625 | -54.81365 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54c08cad-956e-34c6-9ede-6392774ea8f4 | -6.9984 | -59.31587 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66d8a561-333c-3ac6-a1b6-33c5540faa7e | -6.14508 | -59.91708 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 884e16a8-46c1-37bf-b210-fa7ebf997e3c | -7.51249 | -61.38618 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d4e84c7-bf57-3311-b6f3-95bfa0c9f58d | -8.81591 | -62.33761 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a6dbe68-53eb-36c8-9b5e-1bceb83efc7e | -6.62138 | -58.5073 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d586bb0-d23b-39af-8f94-11686ef578b0 | -7.38346 | -55.1766 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54494885-92f3-3fb1-afc4-c527811e17cc | -4.06172 | -56.34092 | 2026-08-26 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6352cae6-e947-3c8c-a90e-ae4e4bb12d90 | -6.72258 | -59.45051 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713ed6b5-06ca-3b6d-9789-c26cd4f4f65c | -9.6087 | -55.11596 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a0a0463-35c7-3d85-b162-726a3509f18a | -6.84637 | -59.43367 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8de224d-2c9f-3f3e-a012-e457fdbbcf5f | -9.13497 | -57.564 | 2026-08-26 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b21ad789-2d62-38ab-82e5-0142aa424ef7 | -8.82097 | -62.32928 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06f587cc-f43f-32fc-bd93-6320599aabce | -7.02863 | -59.23088 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 555f328e-8491-3a47-bbb4-bfba99165907 | -9.20003 | -59.58441 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddabd629-9b97-31f8-8a88-56a7cdf438b3 | -6.32612 | -54.7388 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46356379-bb2e-3ee4-b535-3a2b9a315cdb | -8.1593 | -54.98266 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3216feb6-1904-33d2-9c80-f0497755d94a | -8.2169 | -55.00816 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e93488e5-f969-3926-8989-4986ff9384e0 | -8.17383 | -54.9649 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3761f2f6-bc0e-3e8e-9f5f-72f6bddad3b6 | -6.96394 | -59.08775 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5ff3d4d-3438-367f-9d1a-2d90fc6cb472 | -8.81917 | -62.32697 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3e5e27c8-d936-304b-896a-886915757715 | -6.26909 | -53.38666 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5835b8c0-db5f-3d17-897c-8fb2066b52df | -9.27634 | -60.92255 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84356e59-3ec1-3145-90cb-8bbfb8a2a071 | -9.2932 | -60.92115 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc385711-82d0-3dd7-9de3-8418669285b9 | -7.01061 | -59.23396 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb772828-3f4e-37ab-9944-f72905d64f16 | -7.55727 | -61.41512 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ffe67d3-6177-3afd-8ffd-966a40897537 | -7.01351 | -59.24199 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac52d865-b850-3c53-be28-fcc058771bfb | -5.79272 | -57.61131 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4a1d4e0-763b-3dba-abde-8d8859b2e192 | -9.20131 | -59.57547 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de3d0d59-9139-3a78-b440-c301350aa785 | -9.38886 | -60.57951 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033c8646-6cf4-3864-8ce1-906875153e64 | -9.06452 | -60.43708 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5277d066-17a6-3263-b45b-423603b67d85 | -6.62343 | -58.49302 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87808aa6-09ad-346d-adba-5c1a793a7c62 | -8.82532 | -62.33701 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2cc1c88e-f72c-3286-b8c8-67d09995db47 | -7.38286 | -55.18108 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 498c82a2-4350-3f8f-afe3-56fec7d6ca7d | -6.15017 | -57.94376 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb09289e-5f18-3692-89e7-a6327cea0658 | -6.50659 | -55.22989 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4652feb9-4d60-37fd-9462-1330b880bc70 | -6.62531 | -58.51273 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6d989c4-30ac-3892-aa76-98254482f050 | -7.52867 | -61.38367 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c6d761f9-7b5b-3aa3-825d-0a880ed2dfac | -7.11033 | -56.56548 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22964bed-1c67-3119-a7e0-084b2f6a3778 | -7.02986 | -59.22224 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c37ca5e-da36-396d-a652-6602cab402f3 | -8.1463 | -54.98882 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8c291ab-d34b-3115-9b38-208e014702e9 | -7.39162 | -55.16021 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24622b34-19c1-3e5e-b0ea-af6012aedd0b | -8.63807 | -54.75687 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfed2e82-7d9d-3676-b1ff-17293c93ad89 | -9.1711 | -58.33659 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60764046-79b6-31d9-98e3-24bc95bdc433 | -6.67955 | -56.35013 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a3fc940-4aa3-38fb-84a9-cc2a8cdde444 | -6.72822 | -59.67141 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5c75ff-ad00-327f-84fb-4dcbc1fc1e4e | -7.07414 | -59.22872 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d0225aef-6ba8-3816-a8e5-c4e824ead4b8 | -6.64447 | -58.51085 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c872fb6-bf7c-3b0d-8358-155fef516f45 | -9.17728 | -59.38795 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6e9b074-eef7-316a-9474-970ba6199630 | -6.07532 | -59.97653 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49f6073a-7102-3534-920a-92c605481de0 | -6.86315 | -59.4105 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README71.md)
