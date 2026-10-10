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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ccc4e0a-b18a-3e0d-84bc-30b4120573fa | -7.46805 | -55.70134 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca82ebb4-594a-3145-a0bc-f57042f59cfc | -3.28238 | -54.08229 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3509e44-21c1-3cd9-945f-59aa2712d7e1 | -2.88686 | -54.11177 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad22ab28-dbad-359c-8aa0-4ae9451d6a49 | -3.38904 | -44.48115 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d051a62e-0ef9-31c9-9817-903faf91b40a | -6.67434 | -55.10212 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa873784-0978-3579-bfe0-20dfcc54026e | -6.4673 | -55.05798 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c568c2b-3233-3ee1-915e-6c6ff3ea42f0 | -3.93062 | -55.72565 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cade981-62a8-3d67-a103-3a7a1e54116a | -3.62438 | -54.23861 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d84b90d-2363-33e4-8df6-fbd31066b6a3 | -6.15529 | -47.96474 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd1e17a-ecb0-3105-9762-184cde79956e | -6.32158 | -55.33246 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27ede3c2-ce35-38c3-ba01-29a486f23548 | -7.41809 | -55.2961 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bd9f2e6-16e4-3316-ac9d-15ac7b01845c | -3.03308 | -54.08884 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4361f0d-2776-38be-aa4f-470e84bb4206 | -3.02438 | -54.18661 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21145095-e550-3339-83bd-2dc17d353f09 | -2.42201 | -57.99604 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e13442bb-3aeb-3943-aaf9-d02f6c1179a2 | -2.98402 | -54.1413 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19497a59-1381-3447-b850-4ce9ef6ff4f9 | -1.32271 | -55.45401 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d88a3004-70d8-3f13-88b2-3fc5c136fc92 | -2.47013 | -56.06578 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8db14d1-9c03-3239-a790-cf6297d1d894 | -3.26037 | -54.69167 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b03cc05-5c89-3636-9a11-a3893805a609 | -3.7842 | -59.37911 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00ac9916-918c-33b6-a608-7c06b54f741a | -1.3451 | -55.46922 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 002037f7-8c31-38e9-a4c8-02ce73a47c1f | -3.83874 | -55.79554 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a53c4333-dc27-315d-a5a0-fe279d424733 | -3.16829 | -50.59024 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 758b1de8-6029-3806-9b9a-fb887f81b07a | -3.54967 | -54.68657 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0e17c74-a111-3de5-8aba-9816ffc47a69 | -3.70971 | -55.96805 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0f9a0d0-31ec-375a-ab3d-41c8ba11ca52 | -3.07722 | -58.09682 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec78980e-b21f-3024-88cf-6525bf6e02d4 | -5.0758 | -60.22104 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be49e2cb-d61d-323f-9015-3c2680d539a0 | -7.18559 | -55.17679 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94c1f57f-9d20-3b50-8ff1-ce8e4602a4c3 | -1.05598 | -53.59307 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38864c90-8767-369a-aff5-1deb245b93dc | -1.74176 | -47.16586 | 2026-10-10 05:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7906056-554e-33e9-92df-c307d3334809 | -3.31983 | -54.03873 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d30b0fb3-69f6-3b88-b9a6-2517f2570376 | -1.02268 | -52.43137 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e2e2a665-6b62-3c85-9286-21444a253ceb | -7.38831 | -55.20533 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f542d461-4d1f-3dcf-9441-1b6601c1659e | 0.00522 | -60.57825 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12d0f87b-83b1-317c-b289-b5a20bd3ec6d | -6.32273 | -55.30375 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed825454-9ad9-38de-a7a8-0f44565f145e | -3.39836 | -54.18553 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07c5dd19-44da-3831-9049-b43f999ddf03 | -6.31975 | -58.31219 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9dd5da6-4c4d-3451-b374-ad77a3553eb4 | -2.51216 | -56.14434 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4b6ff8c-b74a-3e99-a22a-2082c1ec9439 | -3.8933 | -58.96685 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa4dd3f-f836-3f7a-98f9-ba1f580a0646 | -3.808 | -49.93913 | 2026-10-10 05:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6141977d-a246-3024-9726-d4abf1e01a5a | -2.85043 | -59.12468 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41d5dcf0-6344-31be-8ac1-0cdf4bba883a | -4.74934 | -55.66956 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8ec6c5-ece9-3373-8822-04155ee46298 | -4.40072 | -43.12606 | 2026-10-10 05:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00d8b92c-cea2-3d35-8c45-32b941feb143 | -4.81414 | -54.7477 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95c6107e-e843-34c6-9cc9-255f8b85919b | -6.33161 | -55.31241 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39e83642-16ec-389a-a3b0-38de5f6b5616 | -3.78074 | -58.58539 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f863e2a8-d115-36bd-8939-bae2c5c8afb8 | -3.0837 | -54.28442 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a4f1c0b-dc35-3e04-83a5-069f9690a1c4 | -6.07239 | -59.88539 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b66be1-87f5-3b39-b042-882061841a7e | -1.87671 | -56.31199 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07ed2b83-af6d-3198-8b9d-680ec2606811 | -3.19917 | -53.85717 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b83212c-4e28-3082-aea6-aa70a528311f | 0.31624 | -60.43834 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eefacd45-1b8f-3975-8505-de91a6df9e71 | -3.10849 | -54.19255 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7934a5c7-a006-378d-993b-e55a511a43c8 | -3.27962 | -54.07833 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5dbf546-3a39-3bcc-843a-cdcc1f8bf3bd | -7.23376 | -44.16686 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fc6e9b0-969c-37bb-a19d-c78384b52112 | -3.25397 | -54.02444 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43520c48-d28b-3e69-a3f4-0fb336cdce42 | -4.84943 | -42.82869 | 2026-10-10 05:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 47f6ddba-da54-34d1-9c3a-2207b77c800a | -2.56246 | -56.16847 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8c7a779-17fa-30cd-b830-74362f55f607 | -4.13856 | -53.99553 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef27a6d9-5dc0-3558-b132-d4e12df5218c | -3.10522 | -53.78597 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bde67d35-8c31-3d25-be16-ae8dae7bebc5 | -7.52958 | -45.31218 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3e97e349-42c1-30d3-a812-c10d3d2dc341 | -5.9562 | -48.92183 | 2026-10-10 05:04:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a201e40-1203-398e-9996-e30d5d07d6f2 | -3.34766 | -50.41671 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 873997cb-3e65-3044-933f-b4363dfe0bc7 | -6.52653 | -55.26101 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3fdd52b-6e54-3ea5-ba14-be6a08c53257 | -3.10711 | -53.94483 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3793f63-79bc-35df-800c-904c7ee3214f | -2.74868 | -54.04012 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f4fff8-7763-3fb0-bb5f-bc342c24023f | -5.9494 | -55.34198 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a11308c1-2905-3828-9b0a-e9ff805d65e4 | -6.04345 | -59.90409 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5795537b-c0da-3748-8f4e-df00db0e1250 | -3.07787 | -51.40973 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c87e72ff-f0ac-330e-ad49-cb8ff8fc1f1d | -3.04385 | -54.15046 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b009574-91aa-3486-93d2-473a781686a1 | -5.67463 | -50.08347 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95cb7dc-a317-3c2d-84e4-a42db58de53b | -6.48184 | -55.95922 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cbb81f7-da16-34bf-9c96-8da115a842a9 | -6.37117 | -55.25409 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f48ab10f-1950-39fa-bbf3-42e9f2998d91 | -5.88162 | -43.41387 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b59499a-a166-3866-b8b4-dd97ebd9a38e | -3.54016 | -54.74621 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 24740f23-fee5-3256-99a8-135558ed41ce | -1.25335 | -55.79062 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bda7fda-156f-3e78-8829-1aa96c3324c7 | -3.00028 | -53.88945 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81a5952-ce61-3108-a5ed-bf7bdf307794 | -6.44074 | -55.05373 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdf93d65-d1b1-3831-a2ba-f31f00b2b971 | -2.99636 | -54.76898 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebc79422-8951-3f25-a8ee-5e645ba81eca | -1.11058 | -54.16985 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0129afd7-e049-38f5-afc3-621d5d3bfeb4 | -3.30657 | -54.01547 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8791159b-ec51-3745-8b89-6feca3219512 | -6.67765 | -55.10265 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b651b63f-9c28-34bb-b6f4-8a461a09e1ff | -3.66765 | -55.54887 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2526092b-1502-34cc-9ce1-807de281633f | -4.554 | -54.97117 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eec39272-2fa8-31a2-8a24-b15bf657c665 | -3.37179 | -57.52608 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc3fed0-561e-3a48-8b58-2484a86a926d | -3.43258 | -54.54689 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc6aca46-bf42-3a0e-8e69-e465fda50bda | -7.21713 | -55.14966 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c526d64-e754-3d46-a4c2-08f2bae5a0d9 | -0.8854 | -48.71664 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083db752-be69-331a-9d66-a39ac580a742 | -5.18405 | -60.30302 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89149c06-7690-3db6-9f95-cdf454a90bbe | -3.5532 | -55.51981 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5a5af8-1664-3159-9b21-dc832489a388 | -1.33421 | -56.40045 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 442977f5-d7be-34dd-b3cf-a18980f54194 | -3.31073 | -53.70911 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0413b5d-8101-3921-9b03-417fa84d94bc | -6.41928 | -51.95433 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 879abbc4-14c9-3eff-b6b4-9ac4d19f181a | -7.08086 | -52.67806 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a95f1ac-3933-3918-8712-b1b0ec0427e5 | -2.51797 | -56.2876 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e54858fc-f60f-3537-b12f-94a0a05d47d2 | -1.2051 | -55.68697 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6500e575-3989-37f0-b08c-981bf85a00ec | -6.43144 | -43.508 | 2026-10-10 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ed7c017-ab48-3ff4-8dbf-27e24763eb97 | -3.02372 | -54.10505 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e72606d0-9dab-3309-9587-e3dcb3079952 | -6.15162 | -53.31446 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 784ebcc3-d231-3aa6-ada3-c54b49349cc0 | -2.75988 | -49.53482 | 2026-10-10 05:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f47d899-54f6-3a71-bc94-1ac3a4402aff | -2.57051 | -56.186 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e646fe3e-aa8d-3e3b-accc-f27c3f636498 | 0.79067 | -59.20136 | 2026-10-10 05:04:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README120.md)
