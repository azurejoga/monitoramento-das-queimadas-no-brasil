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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b508e96d-a24e-3484-a86c-4425dfbf7ce7 | -14.56811 | -48.80135 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65facdc9-4413-388f-b49e-5ac6e42a4d2a | -14.56691 | -49.30075 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a5321378-ea18-38ea-9fdc-c1704cb95679 | -14.56669 | -48.81408 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 412b3575-fc1c-3be0-8d79-d514e2715e8c | -14.56666 | -48.80836 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3caff5ab-3b7d-3b6c-a5fd-842c0abb5d6f | -14.56615 | -49.29774 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22745929-bdb3-3b7c-9bb7-16e2989b3f47 | -14.56611 | -49.30457 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3fa8232a-dfb2-33f1-b502-7ad6cfcbb323 | -14.56596 | -48.81775 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4be3a0ea-2926-344c-8deb-2ea54fc0d7f0 | -14.56596 | -48.81175 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50fb9b85-d864-3fc7-8592-93a51accdfd7 | -14.56538 | -49.30153 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2355936-e54d-33dd-9456-a33021dbce9a | -14.56522 | -48.81531 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efbb7ef9-4d94-3f71-8dfa-6cb8cd70120d | -14.56335 | -48.80193 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e6aa22ce-4636-3489-a2e2-a831ddce520d | -14.56266 | -48.80536 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 58fdc757-8777-37b0-9038-0518c5e6d898 | -14.56266 | -48.79977 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7af03a78-309c-3a50-824e-c976bc90bc41 | -14.56199 | -48.80873 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b97edb3c-1b08-33d0-bb7e-0683fe07e4e0 | -14.56198 | -49.29586 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f669a2b1-2a6b-349d-9e5b-9e8cca7a320a | -14.56195 | -48.80324 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 38021f20-0f2c-3bc7-95ed-db44d0573592 | -14.56128 | -48.81226 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b55089c-dc06-3199-80da-00463ed7a486 | -14.56124 | -48.80666 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 30cc2506-4697-3548-b7d2-ccd354a6340c | -14.56116 | -49.29975 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1a9c994-0ac9-329f-81f4-53c26516670d | -14.56052 | -48.81015 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f3f5d7a4-56fb-3ac6-b32b-60b326ae7496 | -14.56043 | -49.29662 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55048df7-ff20-3687-abd2-824fbf30aebe | -14.56033 | -49.30374 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0bdf94c-abc7-3f2a-a825-b019f932f9ad | -14.55974 | -48.8139 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f888c09-a903-3306-8d13-13bd726b0db2 | -14.55962 | -49.30061 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 093f425a-a17e-3e7e-8fd8-8269ab4cf6a9 | -14.55879 | -49.3047 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56845fd7-8f2a-3206-bad9-ec225c8568a3 | -14.55863 | -48.79669 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a1ef090f-379c-3270-8959-d1d1851c2d8d | -14.55798 | -48.79454 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f1634d91-727f-3066-a4e0-614bb5663b1e | -14.55792 | -48.80022 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0b3aee7e-52ba-3c05-add4-6598a135228a | -14.55726 | -48.79801 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 645b313e-4c75-32e7-9174-6ad28f9dd2ff | -14.5572 | -48.80382 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7a0f9e21-c656-338c-8c87-3aebb40e3205 | -14.55652 | -48.80158 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 17693db7-4e9d-36e3-87ad-362639535a12 | -14.55622 | -49.28801 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 140ea742-8179-3a78-959a-acce0d0a97d6 | -14.55546 | -49.29174 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec986ad2-04e7-3a4f-8a22-65ad9e7e8f83 | -14.5504 | -49.28736 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3769ddfa-297e-3bf9-88df-752ced9da788 | -14.54881 | -49.29521 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96f513c7-1ce9-3d84-9217-c679fedf1eb6 | -14.54794 | -49.29943 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b0553b0-3987-3b30-997c-5149717e50ec | -14.47803 | -49.28627 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c334902-a8c9-3b3e-86b4-0c7ab25bfa48 | -14.4739 | -49.28286 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1e44b3b-319a-3d96-86a3-99d4ddee5c3d | -14.47303 | -49.28152 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 815bacae-f433-32d7-956d-8ae1f7d3e479 | -14.4723 | -49.28513 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c61d824-3c18-3533-add2-1dc49b350b31 | -14.47148 | -49.29446 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57cce7a0-a317-3de2-a832-9ff81637c605 | -14.47071 | -49.29304 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03799c99-b575-3c68-9b77-75aff496b476 | -14.46651 | -49.28968 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40dfc436-f284-3549-847c-91c2ef7feabe | -16.10462 | -50.25274 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5fb0c4f9-6075-3b62-b229-c2f707011e10 | -16.10377 | -50.25681 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90a58063-8211-3497-8912-86962faf955a | -16.10303 | -50.25037 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2afca260-f838-35f2-b39d-233b0cd6e8a3 | -16.10217 | -50.25433 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 504e7501-3614-3e5e-b6b4-e4fef1c37663 | -16.10131 | -50.25828 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9a6227f-c061-389b-a682-1cd5e9cc83e2 | -16.10072 | -50.24205 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c417ce5-9940-374f-8af4-3e69a73eebc9 | -16.10045 | -50.26223 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b318ff9a-6381-3a6c-bf3f-52e3718f5c2f | -16.09987 | -50.24606 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23169bc2-a0b5-309d-8a0b-d7482ed18cb0 | -16.09917 | -50.23984 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2066da3-eac5-3589-b15e-a6f8e381da9f | -16.09831 | -50.24378 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35037415-8331-37ab-a0c9-66ddf9078313 | -16.09747 | -50.24766 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48f5f4f1-cf85-3a27-b0cb-574b67a8ca95 | -16.09656 | -50.26179 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b092141-20ee-3fea-b64e-991c0256c930 | -16.09585 | -50.23598 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90248f86-4274-3841-a744-9a5fcbbc8eb3 | -16.09501 | -50.23997 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1c34fe68-3562-3ffb-9a23-7008cfcc9db4 | -16.08921 | -50.23833 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7077ada6-f87d-33d6-854e-c20f3864ecf9 | -16.08835 | -50.2424 | 2024-10-05 03:51:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b45fe401-6aa0-39c1-aace-9da82f885b04 | -16.08741 | -50.24685 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 27d9b8a5-de6f-3b58-9e37-53b9ecc20286 | -16.0852 | -50.25729 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c467029d-a9f8-33e6-af7e-11c40f49a310 | -16.08422 | -50.26194 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 658a1c23-993b-3919-b275-8e76d885094f | -16.08114 | -50.24741 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f6f9a75-eeec-32d5-937a-d2e7172f40a1 | -20.09347 | -50.16083 | 2024-10-05 03:51:00 | NOAA-21 | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e14ca767-94d3-39ab-a7ba-49ea2391ce8f | -13.62652 | -51.26469 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 15e30848-7e3c-31fe-9068-455d1049de89 | -13.62628 | -51.25994 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 181013e7-8641-3fd5-81d5-ec13f8968d13 | -13.62531 | -51.27044 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 123de896-3b5c-3e2d-bbb8-b2e8ff74a08e | -13.62505 | -51.26566 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2782b1df-913b-3ae0-8641-a477edfa7ba4 | -13.62381 | -51.27138 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3c5922c2-3e09-32dc-a8fb-ea8f431fd505 | -13.62 | -51.26326 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 956927ca-7cee-3cb2-9fbb-668aedb12057 | -13.61977 | -51.25853 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4613048-6c87-34c8-82a8-9988671ad14e | -13.61879 | -51.269 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dea470f-16e9-3eb9-a15e-4c376b9c68c0 | -13.61853 | -51.26425 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 581a36a0-c59a-31df-9370-3779fb098564 | -13.15493 | -51.19559 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4efbed8d-ac42-3cdb-8db3-b53ab4621d43 | -13.14961 | -51.18839 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0bc5c1f5-74c7-3e22-bb75-43d53e83210c | -13.14839 | -51.19416 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0d2e2e1-cc68-3da1-945a-c7d96ad35a50 | -13.14184 | -51.19276 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d78e5ebd-22fa-3ca8-887e-80943045423e | -13.14143 | -51.16248 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e9faf35-5cdb-3aed-b65d-f2eabebde0c0 | -13.14021 | -51.16822 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91a69425-836a-3e88-9761-e195e7375ced | -13.13652 | -51.18555 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4502376-97c0-3a73-9ed6-bc7cc6c6e2d3 | -13.1349 | -51.16103 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ce2a651-af30-3816-b2bb-45e3db5ad51d | -13.13301 | -51.14453 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8e573d41-9758-39e2-b9ed-436934282d13 | -13.13203 | -51.14248 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f354185-b405-351f-8f3a-96d8bc01c197 | -13.13081 | -51.1482 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82af9cad-03e6-3e81-8903-a0f4b44b5723 | -13.12672 | -51.13535 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e570e34-916d-3386-8b7b-6948c8cc6c3d | -13.12648 | -51.14309 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b0d31841-5567-3ee7-a8b6-42be4f34d37c | -13.1255 | -51.14108 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a33877d-f4f6-3ead-bafe-2dad72176299 | -13.12115 | -51.13591 | 2024-10-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f707c44-0fd7-3e23-9547-9ab5814b7282 | -13.11995 | -51.14166 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 60fd7f84-7a14-330d-9d2d-940d612e6a10 | -13.11897 | -51.13967 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 167d903c-f41a-37e6-a16e-575d1088922c | -12.99633 | -51.11945 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed5df6d3-4cfa-3dfe-aec5-3ef564deb3be | -12.99582 | -51.11504 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b18473f9-d0fd-3f60-8dde-7f59e18c4e84 | -12.99514 | -51.12519 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 337b10d2-ae2c-3d6b-be33-042a40df58d4 | -12.99458 | -51.12077 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bccabd36-a81c-354a-b145-fd0dd5f7bf14 | -12.99335 | -51.12647 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91a089ec-c2bc-355f-a8d5-4e507fa867af | -12.98979 | -51.11805 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a82d118-4046-3ff1-9935-6e3cc442f979 | -12.98207 | -51.12234 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 339103f5-efc4-3128-ac86-9ae6e04d3009 | -12.83059 | -50.55716 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d453af3-8f49-38c8-a2c2-d2972a70ed9d | -12.82424 | -50.55583 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1edf3cb1-b029-3652-b06b-3f592246d633 | -12.82312 | -50.56116 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README49.md)
