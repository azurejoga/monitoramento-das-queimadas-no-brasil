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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbbf0c43-f964-3a2b-bd13-1ac3185704d1 | -3.28072 | -54.03098 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d5a42050-dd08-3051-b852-44bc0f4ed01e | -3.67537 | -55.9444 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 434983a3-67c6-3a6a-a693-a74070830f60 | -3.96921 | -55.81826 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e08f32-59fa-3bd0-a441-98f56d67c9a1 | -3.66786 | -59.63464 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88af13fc-d246-3bc1-b6d1-2f07dd4aa8dd | 3.13921 | -60.57823 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c45f931d-0c3d-362b-bcad-542d11bf4706 | -2.94197 | -54.14463 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ebb08b0-51d0-3820-ae37-df06054c9946 | -3.85536 | -55.97902 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e898762b-a97e-3982-b47c-bbd05a497f11 | -3.51 | -54.65453 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c12748-e4d1-3789-bacc-4411f5e447fc | -4.31974 | -50.77903 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d8e2d04-a729-3c6e-a52e-1b976ba3f717 | -3.02239 | -53.89794 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54050177-082d-3ebb-8265-09dc0cbc2607 | -3.08982 | -53.71329 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cb2350e-b93c-3829-b5a8-f872d2560259 | -3.27228 | -50.42906 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 403f6750-a740-31a0-bb8e-cffc0a9bfdd1 | -3.0417 | -54.26128 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37faa5f5-6523-3f06-9621-80334db15b32 | -3.42572 | -57.95946 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77112b8e-04de-34bb-b7d6-c3be4c624c2b | -3.50865 | -54.63344 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1815b9a-e8c8-34d5-a5e7-68d2195c9e23 | -3.05345 | -54.21449 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30ed34f7-f58b-3f72-8cbb-0aedfb1fc1b2 | 0.94397 | -60.4123 | 2026-10-07 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34779279-5db3-3f83-a63a-fa1f1c60ad6d | -3.10298 | -53.7501 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14fd5208-e359-31be-a0ca-34d50e86d887 | -3.49111 | -50.08738 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90784580-70dc-344a-8943-2f3f41f7937a | -3.28785 | -54.00982 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f88b85d-5cc3-3eca-b8b2-2db9f92b23a1 | -3.53164 | -54.63428 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67322248-99b8-3bcb-b51d-48a77158daa8 | -3.99487 | -56.24258 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c44dfa9-91a7-3202-b0af-c67c8bd3cc6a | -3.27292 | -54.04347 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c00b9a0e-5d2e-390d-9b17-ec9beaaa0737 | -3.2755 | -50.40674 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e55b41e6-228c-3741-b564-205f08a8aba8 | -3.27697 | -50.14373 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 25a97d13-812e-30c4-8aef-a554f04015b7 | -3.86563 | -55.99609 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef475018-6d49-3b3a-8fa7-ccc16fb8d16c | -3.00572 | -54.13455 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 984c9e36-faba-3f2c-b0a9-cbbf059a76aa | 1.70787 | -55.64116 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2632082-1ede-316c-9e55-1b71e7407ec3 | -3.09589 | -54.27996 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35fa42b5-69e5-3c11-b26b-cbbad854cf49 | -3.50021 | -51.69175 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ad948f7-d88b-3c87-8f17-58ed55e9818f | -2.78378 | -51.67562 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3050fff8-94af-3a4d-8713-ca0d3e6c2ada | -3.21192 | -53.86809 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce14631a-886b-347e-b453-de338e9597bc | -3.26368 | -50.39893 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 417cf955-c0f9-3361-bd6d-b3fcee006056 | -3.50126 | -54.65104 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29b22e56-47c1-3a97-8a1d-53aca67eb468 | -3.16468 | -50.44279 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed3d498a-bff7-342f-b516-6c55f1d5412b | -3.10185 | -53.7631 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eada92dc-366a-308f-ac69-5b06440237d1 | -3.08514 | -54.28814 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eae8dfc8-2f73-3c68-a06a-6ef7f8cf21ee | -3.50748 | -54.63999 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1252f88c-006a-3a19-9e2e-dcffd1d87b94 | 0.72408 | -51.36989 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e537e88-96cd-369f-9cfa-8c99daf142e9 | -3.65064 | -54.06252 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00a0a8d3-53a9-3eca-8f06-f3f1672d1cbc | -3.28174 | -54.05682 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 571654ff-1092-356d-819e-d628df312070 | -2.83004 | -54.12913 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a647b57a-4d21-3fc4-9875-f5494002c62d | -3.85671 | -55.99857 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0edf72-bf36-3edf-bd1b-f1df35f2da14 | -2.3254 | -60.06668 | 2026-10-07 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9d5006-c9d1-3895-91ff-6840d7fc68c3 | -3.51705 | -58.75936 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 707121a9-566f-3d15-9545-44f013e58990 | -3.59314 | -54.5677 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b519d4aa-42d5-3487-a3b5-f61427f6c3cb | -3.386 | -58.19709 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 181dcf49-5573-31ff-bbe2-3523f5b4539d | -2.85627 | -59.11177 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 876d2f2f-72f3-3f03-86b8-a3e233dc4e62 | 1.71039 | -55.62745 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16325e4d-04f7-3faf-89af-28de8937f670 | -4.46653 | -54.97049 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c43a1a-4315-318d-bdca-dd1a1886b0db | -3.57018 | -59.50216 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4131c27d-d141-35dc-b6a9-ad42a88bd6d9 | -3.46572 | -50.08803 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd739d22-05c9-300b-9056-adb78740331f | -3.07559 | -54.25721 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4321c33-1624-38d3-82c7-3e0f8ce0075c | -3.03835 | -53.92107 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 218c74df-60c9-39a6-bb72-05692acfbb53 | 3.14975 | -60.60157 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66f45c16-80a8-332d-849f-61f727f26233 | -3.27999 | -54.02917 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba822251-1151-343d-9396-8e155c92740a | -3.76674 | -59.4019 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9570477-ae8b-3bb2-ac85-c9205a5ec875 | -2.95267 | -54.06469 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bd527414-4a36-3621-899a-269d51f0c665 | -3.17206 | -50.43433 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c9580c3-7d8c-3a18-b646-36e3f656cd61 | -3.36552 | -58.18539 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36b13b5e-f84d-35f8-a1a7-154d5a6f30b0 | -3.05643 | -57.522 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b6b7d9-0c88-33da-ba5e-946cabf37eb1 | 1.7266 | -55.60761 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9039e6ae-3301-3ee9-892f-a654a07e2231 | -3.06059 | -54.23042 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cd06eab-4b7f-3071-be17-c434b4040a72 | -5.01541 | -50.93939 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b9d0bf-35e2-32ad-bba1-31d3234ec322 | -3.52181 | -54.63768 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f19e192f-5c18-3269-ae17-3ed35dc93d18 | -3.09295 | -54.29911 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6cb84af0-9dea-3bd0-8233-f71c2c6f8714 | -1.80665 | -57.10558 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a164e4e-4aed-3d0b-a14e-5df9df533971 | -3.47331 | -50.07937 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 31cde7ac-9731-33de-a0be-4ee68f8e52b6 | 1.70409 | -55.63862 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aef47eb4-9381-3aaa-801f-d39bb54bc78b | -3.27354 | -50.42028 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de670344-fd13-3082-8fc3-e9edd95c046d | -2.94482 | -54.18961 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ce2480-f1f0-3f6b-adbb-7fa801dae27f | -3.16537 | -50.43798 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aaabe48-4747-3e00-a90c-ae346c4170d3 | -3.54498 | -59.48302 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0478e041-22f6-3050-bec2-3436a631d8ff | -4.45288 | -47.91987 | 2026-10-07 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 99ccac80-fcdb-3b47-a93c-178f0a34e20f | -3.09497 | -54.16085 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6bd6b57-f1bd-3d13-b1fe-de276f8e2804 | -2.13101 | -56.69632 | 2026-10-07 05:40:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca7942a0-e4f8-3cb8-958a-0037067f8693 | -2.92942 | -53.9338 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24cc8f8c-f975-394b-9cc3-b19517a1b28c | -3.27138 | -54.05343 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a99fe419-5d2d-38ba-99dc-d7dd20f2470d | -3.10433 | -54.1623 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c848eecb-b87f-34d6-883d-5988034d0e00 | 1.71356 | -55.62189 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e5621a9-d80f-3a9a-bf79-d17629af507a | -3.64067 | -58.88911 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e626038-0185-3316-a10c-f0ead5e5475c | -3.39091 | -59.59592 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cb69402-69be-3afd-8f9a-a00297e56989 | -1.28634 | -54.56672 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9802f673-7204-370f-b382-d4d7fdf011cd | -3.15698 | -50.43977 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c16dc54-0464-3f8e-9eac-b18756b73b8f | -2.77154 | -54.10519 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 58022bea-7f73-32a9-aff7-60076d33ae8e | -3.1773 | -50.56647 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 25962114-049a-3d1c-b4d3-daf07c0d9588 | -3.27598 | -54.03027 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a512b266-c699-3bf7-923e-5e00aae19787 | -3.85005 | -55.98594 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1c0c30e8-f15b-359c-bb8e-738a45620b3f | -3.38841 | -58.20506 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 614ca3ef-b16f-3c48-a8ba-d98a11193209 | -3.96865 | -56.05297 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a32c7e-bb0e-3c37-bc12-bdb9559443ce | -3.72913 | -55.98378 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46aeb901-d43d-34e0-85cd-5bae3a65d68f | 1.97981 | -60.61026 | 2026-10-07 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 151cb10b-d57d-3584-a335-3c1399d2f95f | -3.63182 | -55.28242 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0bde7da-355f-335c-b66f-18ced5a6ecb5 | -3.08633 | -54.24911 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56c1e524-a195-3362-9add-780ce0f1d6dd | -3.28077 | -54.02417 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3a6417e-0d55-3e86-8405-b64f80c967e6 | -3.6627 | -54.28309 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31c7962f-0458-3e62-b7cb-47502919c9e1 | -3.02052 | -54.13178 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db5eea1a-503e-37a8-9372-25843343b640 | -3.27051 | -54.02778 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5f555e-cad3-34a5-a4d9-3107e9520e48 | -1.79838 | -57.10889 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 450eb4d2-2ede-3155-9614-69c68b600871 | -3.16977 | -50.43663 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README101.md)
