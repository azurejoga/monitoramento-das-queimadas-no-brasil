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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77eab498-fb7a-39a3-84d4-6574b8600555 | -6.34092 | -61.80839 | 2024-10-25 16:52:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 813a001b-ff1a-3a3b-aebb-c7659cbf595c | -5.81827 | -61.5564 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| e0ee5176-08ab-31a2-ab8f-97d50db6a2ab | -5.81766 | -61.55198 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| bdd2b899-134f-326a-bcca-807130cf5896 | -5.64133 | -61.04718 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 41714587-af6b-34e4-be4a-fbaa82a5a5c0 | -5.59471 | -61.48189 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4790df26-b05b-3bd5-97a0-a178bc248238 | -5.58875 | -61.48269 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 29874861-30d1-3cd8-8a5c-f48b751bd039 | -5.49298 | -60.74774 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 43dd9cc7-eacc-3405-9867-5b953431e0fd | -5.49243 | -60.7438 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6fdcb983-2464-3318-90a0-971f15208b68 | -5.35356 | -60.70373 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 62ce1233-2a2f-3a7e-b0f2-851b8bdb3926 | -5.35153 | -60.70693 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 114b7de7-8e9f-30c4-9702-a18f68e28224 | -5.351 | -60.70308 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| ab23c25a-139a-3dec-8eb8-aef619aa0f89 | -7.86951 | -61.688 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7ccbe9ae-6c27-36eb-b56f-114e1791d5a1 | -7.86885 | -61.68297 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1b9e3339-2906-316f-93c3-018f18e8f699 | -7.84512 | -61.64598 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 79382505-ac95-3103-abf2-2eec54fe3deb | -7.9833 | -61.59997 | 2024-10-25 16:52:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1c800b31-8802-362e-b8d5-093e07fb3b95 | -7.86534 | -63.73876 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2ea58480-9970-391c-9840-682fcfb65bbd | -6.93797 | -63.03624 | 2024-10-25 16:52:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f6d756b0-7a82-36e0-8282-d6f058210179 | -6.93444 | -63.03925 | 2024-10-25 16:52:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7088c4f4-cd64-3f49-8475-502ffbe533f7 | -6.52 | -62.97313 | 2024-10-25 16:52:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6c6c9323-d5eb-37c0-88b5-d24017a97ef2 | -8.5732 | -63.05683 | 2024-10-25 16:52:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ac8629c0-335f-37fb-b582-9f71880af1cb | -8.55786 | -63.1127 | 2024-10-25 16:52:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| db914cc3-71c1-3fe3-98c6-ae36c1dcfde8 | -8.55705 | -63.10647 | 2024-10-25 16:52:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 3ce8a19d-4650-3106-ac55-dc453fc0f663 | -8.55624 | -63.10015 | 2024-10-25 16:52:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 165.9 |
| fe065ff6-68ea-3b09-89df-11c47b1b7897 | -8.258 | -62.8532 | 2024-10-25 16:52:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1dcf1ce4-58d0-36c2-9ae9-e053312b2c98 | -8.17661 | -62.85643 | 2024-10-25 16:52:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6541cea4-aee6-3eb2-a810-72127e78d330 | -8.13884 | -62.96103 | 2024-10-25 16:52:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.5 |
| a8b3412c-cd65-3aeb-a491-60faa35ad402 | -7.94922 | -63.69621 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d9cf1cb1-d00f-34cd-9460-7ffacbe52037 | -7.944 | -63.69957 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 477cea36-23c8-3dab-98cb-6038ebbd0617 | -7.91586 | -63.70274 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 16c29381-c4ff-3b81-9b0c-c7c953a97533 | -7.8988 | -63.72137 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 777b98c6-c0a8-3adc-bf55-9f8645767656 | -7.89727 | -63.72532 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| edd914c8-ded8-3623-9c6c-52dcd147096c | -7.89643 | -63.7186 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bc5680d1-ee83-3a2a-ad91-054583c6cdb3 | -9.95937 | -63.62746 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e4cbbf1c-35d6-3270-ae34-c23e956d544a | -9.65256 | -63.60606 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 50bb6651-71b4-310a-9c7b-12b994677dce | -9.65171 | -63.59908 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 130f77f9-795a-39c4-bdb8-92f7766a6a4d | -9.6496 | -63.60734 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5e60cbf0-1546-3d84-9ae8-11e205e649fb | -9.64878 | -63.6003 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3e65a2d8-1dea-332a-8db5-9bb61e489376 | -4.17542 | -63.17793 | 2024-10-25 16:52:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7f3a3549-9f4a-3371-bf10-61c08f764253 | -4.08152 | -63.26427 | 2024-10-25 16:52:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a020c0f7-5f4f-381f-89e9-37a29c77e372 | -6.49201 | -64.29446 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c24db77-e7d1-3fc3-8bcb-08686368f26f | -6.48807 | -64.29262 | 2024-10-25 16:52:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15c91d79-64df-3cd3-80e9-3760390c6165 | -3.67185 | -55.45833 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 374d826d-96aa-3564-b337-966e186e68d1 | -3.63649 | -55.51257 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d810307a-b604-3676-86b1-855482fe8b3f | -3.63332 | -55.5179 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| f8faa15b-784f-30a8-b5e9-f4742f8d47c9 | -3.63261 | -55.51308 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 1d9237d4-f023-3074-b306-d85d920cdbfd | -3.62874 | -55.51361 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 9ab6b3a3-c31f-335c-9930-9f126793dca6 | -3.57725 | -55.60372 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bedc538f-361a-3e06-90bd-05c8e2cce7bc | -3.56532 | -55.41887 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ccdb5393-5fc3-3337-bdaa-13abf7ecb86a | -3.56263 | -55.45327 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b51dd1b4-0882-3e79-9401-7329d7467239 | -3.55877 | -55.45376 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e2692c56-e611-344f-966d-d73faacaf331 | -3.55806 | -55.44903 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b63bfebd-5719-327c-bb86-0d61c00a4641 | -4.38823 | -55.6058 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 02fcae2f-2a21-3402-af43-2b76a26869b2 | -4.38796 | -55.60291 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| efb42aef-a6c8-3efc-a841-87575fb57a09 | -4.36751 | -55.92803 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 28817754-44e4-33d3-bcb6-e54163eeb79a | -4.3665 | -55.92112 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 1cb0e008-f93e-3695-a3bb-084b77bbbab1 | -4.34437 | -56.27967 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b3c8943d-31cd-3fe6-a1f9-d76a2fcb7a22 | -4.34382 | -56.27604 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4236b94a-eb04-3301-b858-6ea60e675d1e | -4.28881 | -56.27235 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9f8b3763-b327-3063-b7ff-710dfac51be8 | -4.28471 | -56.27301 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f470fd31-956b-3483-8d32-2a4b0f4e778b | -4.06342 | -55.55029 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7a89a13f-712a-3104-811b-509c59bcd0b1 | -4.06295 | -55.55267 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 76273170-e917-33f4-bdf4-1a34ececec28 | -4.05379 | -56.28456 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| cca28a4c-ba20-37a6-9a61-5a445bfbdc35 | -4.00748 | -56.25406 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1bca88ae-aa4f-3062-9231-61e97e0afb41 | -4.00209 | -56.0797 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f00884d1-6c7b-36d4-a03b-184f1070a605 | -3.99859 | -56.08382 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1e529f78-d897-37b5-b732-3815fe917c5f | -3.99805 | -56.08022 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 111a1d72-4b70-350d-bef5-bc481b31d5da | -3.92209 | -55.92723 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a31438e-f124-312a-b031-90b880ad94c5 | -3.92004 | -56.17229 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77eba420-5551-374f-b419-b54c97922f51 | -3.80297 | -55.37416 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 0f8edca3-0cc4-33a5-8f16-f6efd294b82a | -3.7403 | -55.99738 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9c83118c-96a9-3761-816d-ed9ac14fbf7e | -3.7368 | -56.0013 | 2024-10-25 16:52:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 37e267e6-1cac-388f-8bca-925ba92742bf | -5.07764 | -56.22914 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c5b416ce-c8ef-3ca7-ab24-4eec882daa05 | -5.07709 | -56.22544 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| e848149a-440f-3ce2-97ec-3e94cf72c699 | -5.0735 | -56.22975 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ea37d438-066b-34e2-a6da-af824979f98a | -5.07296 | -56.22606 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0f1832e3-7266-3194-ad32-0a29c7577337 | -4.99951 | -56.03716 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07bf93f5-6941-30d8-9462-9f0ab619417b | -4.89041 | -55.83135 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b8a8c16-240f-3845-82fe-35ee72f35983 | -4.85941 | -55.90836 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 002803a4-65ac-3d64-8f25-f6362d54edc7 | -4.83565 | -55.80469 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8fda53fc-c3ec-3306-b5c1-e6a00f8838c4 | -4.8322 | -56.08834 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d4d01ba-4c54-39bf-9c95-e774dcec372f | -4.81919 | -56.0563 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 6cdb3549-a012-3579-a516-140449a769f4 | -4.76391 | -56.04944 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52792509-ef58-3aca-9ff4-363f3b88ad72 | -4.69188 | -56.09707 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a8f9359-f18e-3518-bff5-f84a6daf9009 | -4.68823 | -55.73442 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae64c29e-4819-3257-8db6-e7dd4a5b469c | -4.68155 | -56.36332 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9bc2a44b-1016-364a-9597-da84d5c0676b | -4.67741 | -56.36402 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dff2749b-f3c1-3a7a-96bb-581a4b3eb2d4 | -4.63704 | -55.78894 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2905f573-1d26-375b-b7dc-a63bb9aaf330 | -4.63501 | -55.78822 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 00d234fa-f500-30c4-851c-e9b8bfabf5f8 | -4.63306 | -55.78955 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1b445c0d-bdd7-34aa-bb4d-ec50c1aa113c | -4.61346 | -55.76772 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 185af252-1500-3bd7-b281-dd9e5c6bb5dd | -4.61295 | -55.76428 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e963e744-422a-39f1-8dea-7ed1b5047148 | -4.60947 | -55.76826 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e6441ce4-37ce-3851-8c8d-a5f887ab759f | -4.60895 | -55.7648 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 105c0451-4d6c-3901-ae3b-23b56d274ffa | -4.60843 | -55.76135 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 14cc60f5-49e7-3fb4-bf8c-c27fa1f13f67 | -4.60496 | -55.76532 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3071bcb0-c44e-3f3b-9f16-ab1d276e182a | -4.60444 | -55.76188 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 22b541e4-39cd-3f3a-a486-875394253841 | -4.6044 | -56.09561 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| cc8c1b3d-840b-305f-8129-a0d5ae1ff063 | -4.60036 | -56.09639 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 7e4110f0-3edc-33ff-8283-4ee0f1795081 | -4.59684 | -56.10079 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 6c52c4f1-b52f-3fcd-967d-c3e4f0ec4180 | -4.59632 | -56.09722 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |


[Clique aqui para ver as próximas entradas](README180.md)
