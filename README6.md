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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e5c7f71-d31a-37d7-ab5b-c5945a902a39 | -4.41939 | -55.47634 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 37dc9b72-2f6a-369a-9f8a-d4cdb4aac7e4 | -5.86767 | -51.94916 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56ccc1bf-b7c3-3336-bba2-0ec0f9a6b149 | -5.88796 | -52.28589 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b4a516a3-de3f-39b5-8e79-913d357c1503 | -1.04516 | -47.3603 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8815c4c1-fec5-332e-8288-1ec8af33d14e | -6.12577 | -52.7595 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 154e2e6b-c180-3f23-b058-b5299975be25 | -3.14976 | -57.6797 | 2026-09-23 00:03:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a98890e1-1bd8-3aad-98c5-aa09b5fb4525 | -5.04752 | -49.22953 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1df5da08-0463-325b-a66b-17671190cbdd | -2.23376 | -48.75552 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a1e8d04-6136-3677-95a9-86c6aefe0f01 | -3.21674 | -46.94072 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 192b348e-d66a-3407-91c7-fb1724db2a94 | -6.56627 | -55.40694 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2ed3da31-b96b-3d8e-86ee-084629f25711 | -4.17221 | -53.66597 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 684e5ec6-6307-3a16-9de3-75d7ab33ecb0 | -5.73906 | -53.46414 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5da0e441-5c30-34e3-b627-84e56823b2d5 | -2.87107 | -49.6345 | 2026-09-23 00:03:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e11b140e-c76e-3168-adf6-17cc1f2e0e53 | -4.28883 | -48.61825 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 964a1bac-22c5-3048-8c2b-deae9625e962 | -3.10563 | -60.71537 | 2026-09-23 00:03:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| e619b4e8-f92c-3374-9492-d1610cb961a0 | -5.41431 | -49.27999 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4d40acbd-81cc-368c-8544-236cd704c89a | -6.09603 | -57.66637 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b8120f9b-8d5f-389a-9e22-c4413d602b64 | -4.65288 | -50.65734 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| fc7607ac-ad64-36f1-a9e1-e8fcfeaec5fe | -2.9505 | -54.07821 | 2026-09-23 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 582fc1b9-f768-3472-b474-6fd99bc4fe1d | -3.5915 | -50.03284 | 2026-09-23 00:03:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 06203b14-f29c-3c5a-b1ac-3a8865c5a99f | -3.68359 | -60.5581 | 2026-09-23 00:03:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| d333effd-76f4-3182-b135-d16a1f568c42 | -2.73756 | -51.54182 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da23a58e-6a83-318d-9221-75ad08ea1cf0 | -6.64297 | -50.92618 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 188c3347-e9df-3ce8-9522-7e5db8e3613b | -4.46049 | -47.93137 | 2026-09-23 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b9f65382-3db9-38e5-a9c1-2f7c4c02dbe8 | -0.51092 | -49.16182 | 2026-09-23 00:03:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5a85477c-5e65-3804-b0e7-039624bfcf48 | -6.67318 | -50.94466 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ffcfa4ff-93b2-35eb-bf4c-095b989ddf45 | -6.61332 | -59.95161 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| c566412c-779b-3377-bac8-0b10110b3db7 | -6.6657 | -50.8889 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fe26eabe-b191-3f79-9f02-15d4c5ea0e5a | -4.32386 | -55.44615 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ba01b461-6ef2-38e6-b7a2-7e49c2676c28 | -1.13505 | -47.71886 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 146b7543-ada2-3107-bfa9-ee44d8165d48 | -6.09934 | -57.69282 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e7e71812-a678-30f0-843f-719eea32adba | -1.9143 | -58.25854 | 2026-09-23 00:03:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1da96b86-5448-3e61-9e17-f683b1d46fc3 | -5.61063 | -45.93866 | 2026-09-23 00:03:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 45a059e4-d577-3a01-8afe-b30365dabc1f | -5.89575 | -52.08952 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4d8bb1c3-495e-3c9f-b10f-8d92a02fa328 | -1.91761 | -58.25291 | 2026-09-23 00:03:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| a50df948-9c51-3310-8a3a-5065754066fa | -6.89674 | -55.32199 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 20bee3e1-0ac7-3b65-8683-b7ff534ea412 | -5.14154 | -50.05792 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 443d9ee1-6cff-30d8-a7f5-f11fbd5e9cbc | -6.52825 | -51.50479 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a5762b58-1ad4-374b-86a1-52a84af5a0c9 | -2.89892 | -49.16586 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| db7afbb4-f5bf-371b-a710-5f4d4e7197a0 | -3.80715 | -52.37103 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6ee774fb-51e6-3bf2-8630-6b90197d1868 | -6.06865 | -57.80642 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a9fcd8c8-2786-3081-a402-f3b43f4f7a3d | -4.57723 | -45.64896 | 2026-09-23 00:03:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f0b0a0a8-53ae-3fb5-9861-f8e78ffb85c1 | -5.87891 | -52.07682 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 22e8094f-cf90-35cc-aef6-d7be4a6f098e | -3.66133 | -54.26267 | 2026-09-23 00:03:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| db8caea7-aaa5-3c94-835b-960e78283ea1 | -3.22839 | -46.95074 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 249.1 |
| c4c2804d-6d31-3390-a40a-5a814cbc67e8 | -6.60719 | -59.9175 | 2026-09-23 00:03:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bafb80b2-09a5-31c8-8809-a15d43547a03 | -3.22678 | -46.93908 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 56404a23-bc30-3066-b925-db8aaa4cd6a2 | -5.81961 | -52.06422 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b3bdcbaa-3ff6-3488-b4ee-ecbae2896ae0 | -6.62978 | -59.95656 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e4630cb0-74dd-3e86-a96c-76a619dab590 | -6.57572 | -49.8939 | 2026-09-23 00:03:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bad04db2-42fa-305f-96bc-d29cf4e1b956 | -1.29126 | -49.46757 | 2026-09-23 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a268dca-43b8-3e4a-a378-163da27e50c1 | -3.54158 | -59.62294 | 2026-09-23 00:03:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 59cc9462-d971-3560-986c-36889adcad64 | -1.72073 | -49.98309 | 2026-09-23 00:03:00 | TERRA_M-M | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fb7d24d5-119b-34f5-ba67-c205abe9c5fa | -5.20201 | -50.08799 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4cf033f4-0b84-3f27-a3ad-928101a79969 | -5.80183 | -49.1555 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| bb88ae30-5cd9-34f9-9262-251469c31d06 | -5.28596 | -60.21093 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e2b72861-952b-31c5-bcaf-148971fa14e1 | -6.74849 | -50.68394 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 11abea49-edad-3195-a604-d79fd064aa82 | -3.39487 | -50.82739 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 455ef5cd-27bd-36cc-a68b-a5dd14f8b0f5 | -3.24166 | -53.95839 | 2026-09-23 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8927eb22-a4b0-3340-9b7f-d0c26544a5fb | -4.05384 | -56.30343 | 2026-09-23 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7f194c2b-2657-38cd-abe6-18f2ebd73f54 | -5.34622 | -45.1622 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 5283634d-e862-33d4-a036-4b51cf6143c5 | -3.20524 | -50.9201 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 803a4a9c-e843-37a1-a516-b0160546d9fd | -1.63083 | -55.12021 | 2026-09-23 00:03:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b342fefa-b6fd-347a-ad94-4bf760127e7d | -3.93711 | -43.00411 | 2026-09-23 00:03:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 3b7cab44-7f1a-38a7-b649-9ed29870f3f5 | -5.2787 | -47.26426 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b847fd26-677e-3af5-b297-bb3f44160c06 | -2.95215 | -54.09059 | 2026-09-23 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5fa7d2c6-20dc-3dc3-a941-ff952b331e4c | -2.46443 | -57.91651 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 45dbbb02-52d2-3f90-82a3-e629c10f6283 | -6.58092 | -51.49173 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2ecb3872-c3a7-333c-a478-a3c7f1c9b785 | -3.4763 | -59.56834 | 2026-09-23 00:03:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| bab46f0d-e00d-3c12-93d2-48ef3ad7177e | -4.05731 | -56.31694 | 2026-09-23 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 284a9a19-953c-370e-91ad-f4d4dee6aa8f | -4.26758 | -55.44292 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4011ed1c-3cbb-3a93-92ea-a7edb1ef6e40 | -1.13353 | -47.70773 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5fff5fcd-52e0-3107-a106-4fed5a0e4c3a | -6.43417 | -48.46619 | 2026-09-23 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 549aff66-5f99-32ea-860d-ca0e23f2faec | -0.5096 | -49.15235 | 2026-09-23 00:03:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 92aadc79-4bdb-376c-b44d-ea7f68e73612 | -2.76599 | -57.03225 | 2026-09-23 00:03:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 14262d54-2c6d-3301-95d3-e09af997bae1 | -3.80583 | -52.36107 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 08a4b724-dd65-3b8e-907e-0910370138b7 | -2.86106 | -57.78424 | 2026-09-23 00:03:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f9c3a076-a500-3dbd-b449-6c769ff7518f | -5.124 | -48.79134 | 2026-09-23 00:03:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2d0052ce-12cd-3e3b-8061-c62ab0693346 | -5.77434 | -43.77707 | 2026-09-23 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bc5e91ce-8a87-374e-8f42-8d3b6c1c8008 | -2.10646 | -49.6996 | 2026-09-23 00:03:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d6b62c03-9ca2-3163-b635-77c7319983d8 | -4.44962 | -55.0803 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 34e127d5-153b-38d4-8f16-8d6f22bafde7 | -3.72171 | -49.04447 | 2026-09-23 00:03:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 09fc9952-4fdd-352d-8e14-44dc58ce73ce | -5.87646 | -52.12952 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e8cd1a2c-18cf-3cac-95cb-7d5c02f0f644 | -3.89175 | -51.96453 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e08e9cf-3d6b-3a4a-8914-583405d9f8d3 | -3.15164 | -48.07098 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3861fab5-71f9-30e8-83c0-1505c9723fbd | -3.93992 | -42.98692 | 2026-09-23 00:03:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| e3fc013f-d72b-32a0-bd88-2b40af928f8c | -5.86635 | -51.93915 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ca20ad8-fe9d-36c2-8d4d-4afadb28ef4e | -4.05644 | -56.32254 | 2026-09-23 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6af11ea0-35bf-3fdb-a869-6f6429111981 | -2.86985 | -49.62561 | 2026-09-23 00:03:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| a5708864-beb2-3e6e-bf1a-85f74f6db74f | -5.8877 | -52.10151 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a1d9f990-5c60-3331-af5f-13a7175f3e8b | -5.41308 | -49.27112 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ce3cd1e4-b2be-3f82-af91-bb930f7101fa | -5.12526 | -48.80044 | 2026-09-23 00:03:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| a30fb7cb-d498-34b5-82d7-721d772edb15 | -4.44751 | -55.0649 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 63acf069-3c00-35cf-8e54-a476d0fc12d3 | -5.75483 | -49.95598 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f85c0ffc-764e-3620-97c5-55f3c5a7373b | -6.44186 | -48.45587 | 2026-09-23 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 391b7b86-989b-39d9-9448-7275bf02abb7 | -6.60849 | -59.9105 | 2026-09-23 00:03:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 48e22ce9-8e5c-3005-960c-5096f195e9aa | -4.28754 | -48.60892 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 64ec650b-2662-39d9-b6d2-e0f9df7ac32e | -1.63273 | -55.13426 | 2026-09-23 00:03:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 12a857c8-1bb3-3122-9ff2-90e13becb224 | -3.68287 | -60.56321 | 2026-09-23 00:03:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 43a718d4-c46a-3407-9052-989e48cbc1da | -3.86068 | -58.82961 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README7.md)
