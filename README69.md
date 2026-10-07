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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aed880f-33df-3db4-99d4-99971f11467a | -3.03479 | -51.13723 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29a7736d-b4c9-3099-af7b-c77dd21f6e65 | -3.38141 | -58.24052 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9983a295-72f2-3d8c-a0d1-395e77540897 | -3.85312 | -55.84275 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 902d41cc-4eb6-3d0e-8a6a-34befa20cf1d | -3.58475 | -54.31061 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a6c3c8-f5ad-3735-a980-2f16e1ee100f | -3.17177 | -50.44625 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eacebfdb-7cfa-3ee8-b834-62fbe835909f | -4.92133 | -55.86725 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 806fca61-65b1-3862-90a3-a2f4a121a492 | -2.9913 | -54.05711 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29d9086e-14c6-3645-9bde-3b9b2842cadb | -3.66348 | -54.28681 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44557a4e-4725-3e4d-a5be-38f32db98a50 | -3.19348 | -50.56478 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 93b6b5b9-96ff-3d74-98a6-613f0a867ed8 | -2.41371 | -51.29986 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 708bc8cf-be6f-3b1b-8189-5665d124c5eb | -3.04539 | -53.88426 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5137f34-c632-37fa-b3de-998deb8b1235 | -3.11067 | -53.77378 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6fa73dd0-d0e1-395b-a072-3998882d3a76 | -1.28885 | -54.56956 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f5e592-773e-341e-8a6c-9409e3809f49 | -3.75871 | -61.17739 | 2026-10-07 05:04:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6530d38-2c63-3df1-8664-4206b30e184d | -3.09379 | -53.72717 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0e882fd-e10c-388b-8e55-5f06ae7f6bd5 | -3.05602 | -54.14628 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed63b837-8cd2-3694-9541-119c1eb402c7 | -3.04489 | -53.90967 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeb4b9ea-d49a-3fde-8fde-caab9a5f4f2b | -3.06263 | -54.23342 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 878d2d76-2e71-3973-8939-6c616444c5fc | -4.7707 | -50.81427 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e6a7f22-2ceb-3e26-93b3-83ad288fca41 | -2.78795 | -57.65773 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dfa2e9a-c80a-3f24-9899-b3bc49141d4f | -2.76229 | -54.08644 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e2690875-0b43-3f66-9440-1237ae2f88e5 | -4.16003 | -55.14205 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 813f7da5-5630-35f7-987b-5213e40800c9 | -3.1001 | -54.16742 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bdfad14-fa42-3047-94cb-691141222c63 | -3.54272 | -50.09142 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7380482-2b26-30e8-9a26-0903eb4174b5 | -3.22161 | -48.81635 | 2026-10-07 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e017e5df-e04a-3556-94fc-ddd8df9f18db | -3.05065 | -54.2244 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8dde914-2269-3eb4-8476-22d73f20fdf6 | -3.04787 | -54.22038 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3005a24-312f-3ee0-b61d-b92768a33c56 | -2.94234 | -54.11102 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fdfa817-5046-3874-99e4-6fdcf5c5ad44 | -3.72838 | -57.15283 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13073126-41e8-3447-8f3e-a4ada509a46b | -1.29651 | -54.56373 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8fdfb87-2217-3d3f-bdc2-5221b1d618b4 | -3.27684 | -50.78754 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c824f2c-2c82-3fc1-beac-b23c6efeed42 | -3.69114 | -58.89208 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d1b427f6-7797-3edc-857b-49cb6e92026c | -6.94219 | -43.67605 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 62971ec7-f7b9-3bf8-bfaf-99a629964204 | -3.5058 | -54.66575 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1821a7c-2205-3899-b750-f5d2c76aecaf | -3.69681 | -58.28746 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf77a81-5f77-3819-b6ef-d7a2d519fecc | -3.11402 | -53.7523 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 847cc4ce-e2aa-38a6-bc84-c1de41291133 | -2.46671 | -56.06845 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31251b09-2678-32b9-aff7-a019f81f2806 | -3.27601 | -50.42002 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be1e950d-3dc5-3a5d-a866-9bc6ef307242 | -3.73541 | -59.4421 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1a37502-2aa2-339f-ba04-c011e88e95f1 | -3.0806 | -54.29341 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a80a380-2713-3069-96e5-b2d7972cd08d | -6.69097 | -55.20703 | 2026-10-07 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e2866b-a990-36f3-83b6-de3047617fa7 | -3.8427 | -50.31263 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1de2b39a-3c7d-37df-ab31-e84e2d7c57c1 | -1.19754 | -54.21373 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5687fa4a-7184-3fee-a423-c4f0fcdd1201 | 0.44408 | -60.53262 | 2026-10-07 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b9a5c81-9618-343c-90aa-7fdd04792765 | -3.27386 | -54.03582 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ce2d212e-fb7b-3e63-b37a-1967fc3056c0 | -3.08725 | -54.29445 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c1af415-b43b-3c3d-904e-ef17e7a1f29c | -3.58755 | -54.31462 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1816895-89a1-3c52-98d2-9498c798b851 | -3.00711 | -54.13158 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93f0347e-11a3-3fc1-975d-b667f3a70947 | -2.8705 | -54.20041 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88681449-82f9-37ff-9782-146f41c63a43 | -1.47741 | -54.53547 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e963fc1-322d-3460-8a75-a2740cbdf7a1 | -3.53864 | -50.09079 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b3ac613-cc39-34de-9f55-88d969ff2844 | -3.03539 | -53.90458 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3654b5ba-568b-38d4-92cd-aad26bf810ef | -3.7937 | -59.32262 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b4e370-e314-31f6-aa99-652b805e9769 | -3.05796 | -59.90795 | 2026-10-07 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c6abd12-6ec7-34f6-a5e5-92d17bdd7915 | -5.48132 | -44.26061 | 2026-10-07 05:04:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 490b6326-ddd8-3959-99fc-c7fe2b266168 | -4.24998 | -51.04423 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b13960ea-f1c6-3445-b7c1-a1cb45cad9f6 | -3.30185 | -42.27425 | 2026-10-07 05:04:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 190c541f-923e-34c0-b164-706c3f0f30ac | -1.10533 | -54.15368 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0afebed8-b40b-3d85-b255-d5f32c5c8845 | -3.87723 | -55.81829 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2bb5c1a-173e-30b1-8eac-d174471006ce | -2.15303 | -51.97969 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13747a2a-5cdf-32ce-bcc5-cb0ed11bc7a5 | -3.00245 | -57.74605 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdbc0410-b5d1-39e0-89a6-b806fcd8077c | -2.93688 | -54.1461 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 82ff9cbb-759c-3984-8ba3-f82ecfacb942 | -2.79228 | -54.09105 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c90417e8-d160-34ce-ba80-5ba6d75eb1e4 | -3.27359 | -50.4091 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b3f919-6e3c-3410-a326-4436b31cfa7b | -3.03651 | -58.66919 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61a682e7-090e-30af-9245-2d74358ad215 | -3.18523 | -57.05714 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6e7b78-bd42-3f75-8bbf-27b1d40fa710 | -3.86298 | -55.99609 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1dabd19-fc65-3b1d-a05f-6c80529c79a7 | -4.54121 | -54.98652 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd96a12f-5a0f-3642-9240-3b49758a5491 | -3.27873 | -54.17702 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f22f6a-253d-34fe-838e-f9f3dc10fea5 | -1.34992 | -52.79381 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ad433b-93db-37d3-919c-d4a2134f5e75 | -2.96801 | -54.20803 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6815c484-83c7-37bd-9e5f-be2e67976bda | -3.09523 | -51.37801 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6838c5-769d-3b20-8452-d3847950dc85 | -3.0984 | -54.15631 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd493d2d-88fe-3c00-ac6a-5ff7aeef8300 | -3.58668 | -55.56488 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93e663d7-6584-3730-b819-41262c0b67b1 | -2.82348 | -54.13174 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376c2118-89fd-3128-a0a6-fd6ceb6511a8 | -5.98964 | -55.36485 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bc61ed8-9176-396b-bcd8-e65db8fbfd18 | -2.9418 | -54.11453 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 127128e9-ced7-3692-a170-cd744bc05a8a | -7.88115 | -44.19637 | 2026-10-07 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6608687a-4ba2-3389-982a-656473768b7a | -3.08593 | -54.237 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 829e96af-4bda-322e-81ca-218c171f45b5 | -2.80296 | -54.13218 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40bfed51-c0c4-38ce-a474-9d9c4fee465c | -2.0369 | -57.05407 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c015a48-9c05-301b-9a32-beeae5ec8df1 | -3.96922 | -56.05934 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d950e34b-ff00-3528-9efc-0926dbd21e7e | -3.29224 | -54.02776 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f19934b1-5dab-3848-a313-bfcd64a6c1fc | -2.7767 | -54.08147 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7f8d0ce4-71f6-321e-b82d-b6de32bbb7cd | -3.10126 | -54.18198 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c62ab22f-9ca0-341e-8474-5dcbddb0797c | -4.15076 | -55.15819 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b653f4-41d1-32c7-af68-4e068d7bd1ec | -3.02572 | -54.51617 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a95d5f1f-db3f-3b6e-b9dc-bd7edc187be6 | -4.28876 | -50.78558 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a1329a9-6a12-3c84-b357-839f7dcbd091 | -3.06254 | -54.21191 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b58ee70b-bbcb-3cad-ad08-a7532a9266b2 | -3.05119 | -54.22089 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc9a533e-d51e-3e84-9dda-5f84785561e4 | -6.75798 | -50.96307 | 2026-10-07 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f553244-0f13-3b17-8f91-a9a1012075e3 | -3.51957 | -54.66434 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42f8ab13-2866-3829-8f1b-52d964e6e23b | -1.79987 | -57.1103 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eaaea4bb-a552-3c38-8262-7e6ee4ec5de7 | -2.93906 | -54.13206 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58d7586d-85e7-3858-8317-1751db9d850b | -2.86942 | -54.20741 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62db10b1-4813-3989-9160-557bccbe0165 | -2.76175 | -54.08994 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ce6d4756-3206-39c6-a077-a3c73cc9e53a | -4.12392 | -50.8143 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc8cf32b-5df5-33d1-bfe2-e8e9af298110 | -3.36024 | -50.76762 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ff04c6d-dbb3-3477-aa0e-bc368e49224d | -2.92289 | -54.10444 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0751bf99-b6a1-3d0e-917b-126efd66f104 | -3.09065 | -54.16234 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README70.md)
