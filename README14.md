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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03026866-937f-31b8-a5f5-047c24549a40 | -3.0001 | -54.1086 | 2026-10-06 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 323241f5-03a9-3346-9a7b-2cb3b9c64f6e | -3.332 | -59.4852 | 2026-10-06 01:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 387f814c-c7d5-39dd-8ac6-0077dc0de98d | -3.0375 | -53.8865 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| dcba11e4-7f09-3b51-b844-1acdfc4ac9dd | -3.6915 | -55.942 | 2026-10-06 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2fa34478-6d1c-33e5-9ac9-e07e4025a93e | -3.0191 | -53.9071 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 09c692e4-c73f-3e50-9a20-ce749d20781a | -3.1116 | -53.7436 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fb4a72f3-c97c-311c-beb8-7cb048cfc3da | -5.8509 | -45.0318 | 2026-10-06 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 00bfc945-a333-39fa-a222-fa8de03e9a86 | -11.6946 | -43.6787 | 2026-10-06 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 51149fef-e8f2-3f5a-98f0-2ac08f7c3f16 | -5.8511 | -45.0091 | 2026-10-06 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 98ab81f7-80d1-3141-9718-6be21f22a27f | -5.8323 | -45.0105 | 2026-10-06 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f03d4535-7e96-375b-8a9d-d19b792079ec | -3.6915 | -55.9618 | 2026-10-06 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6eec7fc2-7563-3937-9142-f9a07b828700 | -11.2798 | -45.5052 | 2026-10-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 1f7465f4-d737-37ac-8034-64ce190babdb | -3.3723 | -58.1957 | 2026-10-06 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 50a5ca8f-8439-32f9-8c2e-be3528b212ab | -8.7036 | -45.2061 | 2026-10-06 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 2e575595-ca6d-3665-af07-52ed8a006fcc | -11.2611 | -45.4849 | 2026-10-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 57a4e6b7-0d5b-3ddc-b9a3-dd9fc1fe5c06 | -3.3905 | -58.2146 | 2026-10-06 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| abff1ef1-2619-3428-81b6-5297ad247796 | -3.0933 | -53.7037 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e04e4f5b-b7a2-3f1a-9a24-a73da5a0bd01 | -9.7313 | -65.0757 | 2026-10-06 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 55b9d3e2-a3ae-3d36-bc85-b8d9d047f911 | -3.0932 | -53.7239 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| f79d0be3-e913-3364-a779-94fcd4af4fc2 | -3.0192 | -53.887 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| c226c952-3b0f-3c3b-b6ae-2160f0c7112c | -3.0 | -54.1287 | 2026-10-06 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e3beaec8-adb3-3408-977d-55582636e615 | -2.7796 | -54.1138 | 2026-10-06 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| bea3c4b5-ec52-3f80-a3e9-f9accaa370e1 | -3.0932 | -53.7441 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 082ca658-5e43-3c36-a218-2b5b6fec50fb | -3.7409 | -48.8689 | 2026-10-06 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b98b618f-5154-395f-86f4-8974b7acc599 | -8.7033 | -45.2289 | 2026-10-06 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 307a3be9-7c00-3d43-a2d5-8c001f9faf22 | -3.4955 | -49.8979 | 2026-10-06 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 48c2f9a7-35dd-33ec-b474-e38489ebaa1c | -9.7312 | -65.0944 | 2026-10-06 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 260ea6c6-32eb-3016-91b9-7babb5939eea | -3.6732 | -55.9425 | 2026-10-06 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 6fd8c372-2e96-3c89-ad6d-838963449118 | -3.0932 | -53.7239 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 4c353f88-d95b-336f-845f-298c02fd1b67 | -3.1116 | -53.7234 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2b2ccad4-d3e1-34d7-8f8b-560c5c5a84ce | -3.1116 | -53.7436 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cb4c62df-9fc2-3b33-b16b-cb7875017875 | -3.0932 | -53.7441 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3615c2f4-3514-3c7a-a398-fb72dabc16bf | -2.7796 | -54.0937 | 2026-10-06 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 5fca4d38-e554-3ae3-ae16-7ac6ff023b05 | -3.3723 | -58.1957 | 2026-10-06 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| d18b4b15-aa4a-3e91-a525-72589234683e | -2.7796 | -54.1138 | 2026-10-06 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6998baa1-750e-3cfa-8c22-25922c87a012 | -11.2802 | -45.4823 | 2026-10-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 38bee3f4-bf9c-3c72-bb33-5d015b5cde4a | -11.2607 | -45.5078 | 2026-10-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a303e2c3-6987-3978-a2b2-fc5bc865198b | -9.7312 | -65.0944 | 2026-10-06 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2f808b13-32f0-36ae-915f-deb3d65ed0ec | -2.7879 | -57.6843 | 2026-10-06 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1204c74f-38d9-3261-914f-2a3eb71269e0 | -3.6732 | -55.9425 | 2026-10-06 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 50cc14df-3ab1-395e-bc4b-b79825e1bca5 | -9.7126 | -65.0951 | 2026-10-06 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a04d3884-02e4-37f5-be78-64af873c39bb | -3.3906 | -58.1953 | 2026-10-06 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 703ec921-a469-3bf9-97db-e197e3ce0590 | -3.0191 | -53.9071 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 16867aa5-a5b0-3f9b-9565-ac7369874601 | -3.0375 | -53.8865 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2d9b8835-c5a7-3be7-acf5-a56864e5f913 | -3.6731 | -55.9622 | 2026-10-06 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 50af1cdd-4558-3851-92b5-998979563743 | -3.1115 | -53.7637 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 021c803a-81e0-33d7-b410-44e44bd046b6 | -3.0 | -54.1287 | 2026-10-06 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 22b4f6ac-e572-337d-a844-c4565f5b0eae | -8.7033 | -45.2289 | 2026-10-06 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 15001709-6324-31de-a7e1-77f24e1324b0 | -3.0192 | -53.887 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 180c6927-d680-370d-96a7-be155864931d | -3.0933 | -53.7037 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 321d7553-fe1d-3f4c-945a-4bb389dba6ac | -3.0375 | -53.9066 | 2026-10-06 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 42d1c34d-0c62-32b4-9d33-b1c1faa5ace7 | -2.9816 | -54.1291 | 2026-10-06 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 829161de-cdef-3404-a7a7-87a2e17e1bcf | -11.2611 | -45.4849 | 2026-10-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1e8e3632-f533-3f7a-bd69-961a3d5fde74 | -11.2798 | -45.5052 | 2026-10-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| ff7a3131-dbcd-3018-b33d-a653c7b97d1e | -3.6915 | -55.9618 | 2026-10-06 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| afab4a3b-9bc8-3eb1-99f3-2b59b64eb604 | -3.6915 | -55.942 | 2026-10-06 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 4becad77-9aa0-3f5b-b9a9-024a0f65dc3e | -8.7036 | -45.2061 | 2026-10-06 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| da5d7633-9e28-3a0e-b062-b817bb5be653 | -2.9448 | -54.1501 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 730a76e5-5df3-3e56-ba57-25bc6dfbe5b5 | -2.7796 | -54.0937 | 2026-10-06 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3b2848ea-d40f-3845-9777-fc916fdbec92 | -11.2611 | -45.4849 | 2026-10-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 73fcc8c8-d77c-3c7a-8d13-097780873d5d | -11.2607 | -45.5078 | 2026-10-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| ae636b1f-794b-3c0e-8be7-96aef1feb394 | -3.0932 | -53.7239 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| fa4dee42-31d1-341f-9420-ceb38ebcc4aa | -3.1117 | -53.7032 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 05d5318c-7a7e-36a4-b4fd-5359c1b380a9 | -2.7879 | -57.6843 | 2026-10-06 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6f236e65-1371-33a3-9267-bc871c2109ed | -3.6915 | -55.9618 | 2026-10-06 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c6f54523-20f1-3b0b-8afd-8b3ad8707f4f | -11.2802 | -45.4823 | 2026-10-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 6a86d8cc-9f12-3d61-8c15-0317441731e9 | -5.8509 | -45.0318 | 2026-10-06 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 9637c34a-79b8-354f-b345-7885c383094a | -3.0191 | -53.9071 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e4c06dd3-31e2-39f5-a0da-f48a92f25031 | -3.6731 | -55.9622 | 2026-10-06 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2a88e02d-2616-3f0a-8206-e1aa3c85b101 | -3.0932 | -53.7441 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 95a2e02e-0e8f-3503-ae77-63e1f7cefea8 | -3.6915 | -55.942 | 2026-10-06 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5c43c693-8bc5-3d26-8936-e3f4791dd937 | -5.8323 | -45.0105 | 2026-10-06 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 17c41c07-38b8-32c6-a724-85c433bee4a6 | -3.1116 | -53.7234 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5e8c1dc9-d0da-3e95-a238-052effd257c3 | -2.8897 | -54.1514 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 813fc6e3-9c01-36d3-bafb-359ceb1bf67b | -2.8897 | -54.1313 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d7a84d87-df20-3618-9c0f-0b25cab9f3b4 | -3.6732 | -55.9425 | 2026-10-06 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7fa8f530-0354-309e-b19f-eb6dc41b6da4 | -8.7033 | -45.2289 | 2026-10-06 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b97e2a67-fccb-3dca-85f3-e4cb9489ca88 | -2.7796 | -54.1138 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6c732595-8656-3b02-b335-e32ab00fc235 | -9.7126 | -65.0951 | 2026-10-06 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7bad6551-f5e7-37f6-9750-95f1c9f6e2d5 | -3.1115 | -53.7637 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 31a1f196-a0e2-33d4-95ec-2160ce4db501 | -5.8511 | -45.0091 | 2026-10-06 01:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a98668b2-e85b-3411-a043-c6a7d8bad9c9 | -2.8713 | -54.1518 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 597d1bd0-6bee-3f86-92f0-89cf513dedc0 | -2.8714 | -54.1318 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| be6428c2-c121-35b5-ba79-ea0cfb73b0a1 | -3.0192 | -53.887 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0ca89c53-a23d-3876-9aeb-9d0229d47940 | -3.0 | -54.1287 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b8b015e0-41ba-31ed-a86b-886b27f466bc | -11.2798 | -45.5052 | 2026-10-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 55cd336b-ba70-31be-a9d8-9e77b35bcbbd | -2.9265 | -54.1305 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 00852c2a-1458-3bce-9110-e41b9c6bd72e | -3.3723 | -58.1957 | 2026-10-06 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 486f3513-c4f8-38dc-a959-a670b1a444b3 | -2.9265 | -54.1104 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2af278e3-21af-344e-b497-565b4dcf353d | -3.1116 | -53.7436 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 80be8822-a03b-3883-a4fd-439eaac10c9d | -8.7036 | -45.2061 | 2026-10-06 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7c01411b-0d68-32ea-9270-fee31972c03c | -2.9449 | -54.13 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a06cb037-c074-3f38-94fb-ca6974f9e7e6 | -3.0375 | -53.8865 | 2026-10-06 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9c109567-70e3-39d9-8624-a12c132b040c | -11.299 | -45.5025 | 2026-10-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 2c9e83de-9653-3bbb-8389-2561b7533f77 | -2.9816 | -54.1291 | 2026-10-06 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e33ab2de-ca6d-3595-bfcb-61d61fd22f00 | -3.3906 | -58.1953 | 2026-10-06 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fa9fbf1e-e902-3347-9f4b-9a607de9644b | -9.7312 | -65.0944 | 2026-10-06 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7a727367-0ea1-3b82-adcd-358eb29a707e | 0.4465 | -60.5442 | 2026-10-06 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b67481e8-05ab-368e-9634-b8c5f2f84857 | -10.8252 | -69.41106 | 2026-10-06 01:54:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ddc4cea3-ba44-3063-a57b-c0f2bc0c89f6 | -8.60308 | -72.73383 | 2026-10-06 01:54:00 | TERRA_M-M | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |


[Clique aqui para ver as próximas entradas](README15.md)
