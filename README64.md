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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60c3b73-1c94-35b3-856c-93f2375e2966 | -6.86376 | -59.47214 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8885707a-4f5d-31fb-8331-ae878d5c22f9 | -8.61127 | -54.77777 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93be8ed5-b9e6-3d13-90f3-2a4c862a1bf9 | -7.97066 | -70.02766 | 2026-08-30 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cdc8b35-a786-32f5-9183-6d12f1c68e10 | -6.93057 | -55.69836 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c882d1d-54cc-318d-a2a3-b670f29fb563 | -7.01646 | -59.65705 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0643097-8297-32cf-b83b-3bbe8ba76303 | -8.66895 | -66.51081 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a9bedb-0197-324a-8bc5-cf77aca48c58 | -6.76868 | -55.66083 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbb35623-6e3d-38bc-a6cc-964c630d4aa0 | -6.93516 | -55.70659 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b6fe0d9-6183-3404-b378-9bf5f4dc51d7 | -8.80853 | -67.28849 | 2026-08-30 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89125530-41cc-3f5b-8532-92f4b9525ed8 | -9.04314 | -65.43075 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b31882-10d3-3cfa-8a5b-0323505617e0 | -6.90697 | -58.98935 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74750de4-b45c-30e9-9c64-12c706243fbd | -9.01432 | -65.40489 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2086a6cf-ee8b-303b-899f-7d9c4d7b4486 | -7.48222 | -61.40152 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 628e4b2d-3a51-3269-9a84-df74839fb166 | -7.30504 | -60.60395 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c325090b-ed7a-3e09-bd45-fb908b42c6c1 | -6.71121 | -58.56473 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1064683-c1a6-31ac-90dd-4dd1f1b3e8d9 | -7.56117 | -61.30272 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc7438b2-6e1b-358a-82ec-f1025d7063e1 | -2.91407 | -54.11567 | 2026-08-30 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fd137de-6c0f-3980-8aec-59deaf30b38a | -7.69923 | -61.1549 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| eef06f80-43d9-359c-9a25-fce465091ea0 | -9.71378 | -60.74408 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb83883-7a0a-3acc-9ae8-453ecd2046a2 | -9.07611 | -64.24773 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 603e6360-1adc-3755-89c5-1372041192b9 | -7.25865 | -60.63335 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 334dcaf3-556d-31a3-93a7-e8285a9ee480 | -9.07111 | -60.49231 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc208e1-e95f-3f2f-b9ca-6e32e5e07af3 | -9.00213 | -65.43893 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c408ddf6-3452-3492-91f3-dc6c52b41d9b | -6.93516 | -58.95269 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 165b2921-bac3-330b-9a75-1388e904cbed | 0.14464 | -60.39666 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c35c147-9555-37b8-b04e-fbb96a93aa27 | -9.2415 | -60.41082 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 159a6aee-5ecb-3fd0-9efa-45be5fa762d7 | -4.08415 | -54.10749 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fc9f658-74ea-34ba-8560-ff3e8dfeb482 | -6.68062 | -58.74933 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26444686-c6c2-3b45-8b3f-8294de9fab8b | -3.2044 | -61.16913 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 923daf31-975b-336a-b9f2-34ca2118ccc8 | -9.01153 | -65.40085 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3febd88-0939-37f5-b3e1-a7722bea7795 | -6.77176 | -60.00934 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7f6d39-1535-3661-8345-9f39c1e99907 | -9.05204 | -65.43936 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 132bfe93-a2cc-3233-bb82-9e8a9c29b7f0 | -1.252 | -55.7026 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a54e614-4317-30c2-8aba-06e6e78ac2fa | -7.31613 | -60.61275 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9346a44e-a68a-3af7-bd3a-7a3eaa9c666c | -7.23953 | -60.6235 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec329d26-7706-34e5-9e98-73107d9080f3 | -2.91344 | -54.1199 | 2026-08-30 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9aaba5d4-2b32-3a42-8190-3f0f03aad89a | -3.20466 | -61.14251 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8386031d-1766-3891-96a9-e67863ade4ae | -9.25472 | -57.52721 | 2026-08-30 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82a0eec-5964-3527-9ff6-933946e647f8 | -9.61121 | -55.1256 | 2026-08-30 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4677c44e-2cf4-31b9-9abd-35f4be48b125 | -3.20283 | -61.1665 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55e2f5e9-3e92-3fe6-bfd8-4532bad051fb | -7.31665 | -60.60924 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd141433-1ecb-3fbd-8113-04a103dfeba8 | -8.57708 | -66.95284 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0554d9a6-afd3-3e70-be3f-55f12adcb9f8 | -9.15703 | -59.50265 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d0945c0-9327-398b-a3de-774168633cce | -7.31209 | -60.61216 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b3b2fcf-b1f2-3335-be81-d71e6b24a75b | -8.25508 | -62.7552 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc563b48-8c35-38b1-86e1-0178c36f54a3 | -9.00546 | -65.43947 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838e137a-c523-316a-a5c6-150c678f31df | -8.94931 | -62.37037 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9dc7bd8-2e5e-3b60-a48e-7aa7d1fb80ae | -9.1615 | -59.5033 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da4d845e-69ce-34f0-af39-3b3decb0e244 | -7.84739 | -62.3201 | 2026-08-30 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44820323-0e26-355c-8dba-b2b7e1f68328 | -9.87233 | -60.2977 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1737a0b-6621-3fc4-bc51-432f4a5c5a01 | -8.99879 | -65.43841 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0f3c9d-ac4a-3ed0-8e3c-6074cc88016d | -8.24725 | -62.75823 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33754815-8fa3-3e16-8106-c0a42289d684 | -7.27385 | -72.72956 | 2026-08-30 05:53:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9cb798-401a-3dcb-98ce-960de0e7058d | -9.15471 | -59.50011 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50c07a82-2398-358d-bcd2-61af97a555cc | -7.9745 | -70.02831 | 2026-08-30 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27d2a912-9432-37d6-bdf5-15084c200e30 | -8.99936 | -65.45648 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5af6b698-6e6b-387f-8187-53919c784eaf | -9.00157 | -65.44244 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17ce537d-8401-30bf-895f-666396a75d89 | -8.94583 | -62.3811 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e1ee631-b6b0-3ace-9c28-32e055890d57 | -6.87449 | -56.57633 | 2026-08-30 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ebb3e0-ebb8-30ee-b96a-fcc1191ab422 | -3.49558 | -54.6592 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d30b26-0251-3c05-9101-dce10ff16d76 | 0.14017 | -60.4039 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25673ce6-f795-3867-83c1-fc27f593c65c | -3.20136 | -61.16423 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4668ad46-2fcd-3615-977f-d577bdd950d5 | -1.25775 | -55.70788 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb67e81-96ff-30fd-b04e-44480ff7f917 | -8.61004 | -54.78696 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 191cb159-8ba8-34b7-8019-c74a48d555fb | -3.25611 | -60.65741 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a120cba-e5fc-3c87-bd86-993ad431cd17 | -9.06693 | -60.49172 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abb56b7-0c15-3fc6-a4c9-97be52c7e163 | -8.95082 | -62.37284 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c0a6c18-5a19-3ff7-9380-06c57db8ef8b | -8.50029 | -55.29199 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f69c9dc3-b866-3e39-9b3b-6d4dc4665eeb | -8.95567 | -62.39159 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a20dc48a-c4a7-3b4e-9f77-b3b7ef37020b | -6.78613 | -55.6813 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f868c4f3-8ecc-35c7-99d4-2e35c74567e5 | -9.14809 | -59.50135 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ca0261c-6296-3003-9696-de543858855e | -6.91139 | -59.48587 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2ed44a9-c6cf-3ac1-862f-11d9eff9231f | -6.76922 | -55.657 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f477dccd-641b-35a8-8d8d-4035a56a9a05 | -8.14859 | -63.9982 | 2026-08-30 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b98126-850f-382d-99d1-3ba74edcc455 | -9.15343 | -59.50896 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62b6453b-1d48-393c-9423-3c93647464d1 | 0.13726 | -60.39783 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 772131b8-9f84-319e-917e-ac91c40f9e9b | -7.39807 | -60.58856 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddd25677-40b5-3d04-8302-6faa0923c49c | -8.63161 | -66.55162 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c1b5a4-98ed-359a-9c55-a3403a669196 | -8.63132 | -66.54044 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada689a8-dbe9-366e-88c0-261c43f8eea6 | -7.84372 | -62.31953 | 2026-08-30 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d55743c-0f88-38f2-8bf2-cba4d7e36761 | -9.01098 | -65.40436 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60fc6bc1-9553-3b5c-8a2a-5b48539f7ed5 | -6.91572 | -59.4865 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 919e9427-bf7a-3158-82b9-5c1b12f88d39 | -3.20627 | -61.14482 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ad328d-99e3-35db-bdac-cff22fa5ff6a | -6.88713 | -59.4037 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 314d1e07-54d7-3a2b-b52a-15b41f84e452 | -7.55972 | -61.31244 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4295753a-7bf9-39ac-b67a-f2a5a974ece9 | -8.61614 | -54.7877 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63929e6-a6e7-3b92-b0ae-9b3f511344c3 | -8.61551 | -54.79241 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2866ea74-9330-36a6-b3d0-b816f11a4ec0 | -8.2266 | -61.42147 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 428e660a-378a-365a-be00-b03f0f096986 | -6.97481 | -59.59492 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b75fd04d-e187-3cc9-b99c-13511eb16e45 | -7.30857 | -60.60807 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a61978-e2b5-389f-a3c9-8a00758a0606 | -6.72372 | -60.0178 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e83ed507-ecd5-33c9-bbc7-5d813845d8a1 | -7.32679 | -60.59639 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 690c7540-40f8-3dee-8fe5-24e8e35ae9e7 | -9.04978 | -65.41019 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4828b1d3-ee1d-3ab6-9d59-d616f59c245b | -9.15024 | -59.49947 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00c066d0-28e8-37c0-abaf-04791d06d9f2 | -6.92954 | -55.7059 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6103a811-5074-3639-9cbc-59a19cf39c0e | -8.66951 | -66.5073 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57052af9-1b06-34ae-9386-ec4e10e40913 | 0.14386 | -60.40334 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c72a11e9-547f-3241-83a9-5a877d59c649 | -7.05683 | -55.67545 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0645a4f6-4955-3474-8073-db7abbe16191 | 0.19788 | -60.50493 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b06eef9-5b8a-354f-b7f2-c02dc1d6fb5f | -7.2355 | -60.62291 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README65.md)
