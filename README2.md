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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8baafb56-0ffa-3c16-9fe7-f67491a74baf | -9.042 | -61.9487 | 2025-11-20 01:09:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98359ccb-fcf2-35f8-afbf-908600eb83ea | -20.735399 | -55.7034 | 2025-11-20 01:09:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5377c1ac-9fd4-32b7-a81f-f2711c2bb329 | -9.0387 | -64.034698 | 2025-11-20 01:09:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b514f70b-65b3-3ddc-9952-a72f97eabf5d | -8.8335 | -62.3004 | 2025-11-20 01:09:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa99b8a2-a8b0-3841-8c0c-17231e102a00 | -10.8246 | -56.953899 | 2025-11-20 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca8c9b7-d910-3d9f-b00b-1c6c354dc916 | -10.8343 | -56.9515 | 2025-11-20 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22a5c1a2-78d6-30ba-924b-8df65569cf84 | -20.732901 | -55.693199 | 2025-11-20 01:09:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b82c3f54-fb63-318f-8a9e-cc43725c39f8 | -20.288799 | -50.983799 | 2025-11-20 01:09:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29fb2e96-9c8d-37bd-a1ac-84f2dc836def | -20.298401 | -50.980801 | 2025-11-20 01:09:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8c60869-d73e-360d-9f19-1f954af03fa7 | -10.6253 | -65.269501 | 2025-11-20 01:09:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae52904e-a967-35a6-a636-963cc0e08899 | -10.8371 | -56.9632 | 2025-11-20 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3958995e-4f20-3341-932d-15fb8f7c5f01 | -10.6236 | -65.261597 | 2025-11-20 01:09:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a54bcb00-042d-3b89-88e1-40a231d96249 | -20.2833 | -50.963902 | 2025-11-20 01:09:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb275776-56fd-3d12-8b42-3acc7fcba4ce | -9.0436 | -61.955799 | 2025-11-20 01:09:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cbd5550-0cf3-37e6-94dc-b97b48881906 | -10.37039 | -48.8938 | 2025-11-20 01:11:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 27831591-4a76-33ed-af81-22363d839794 | -8.83578 | -62.29796 | 2025-11-20 01:11:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d55267e-584b-3349-8106-bad698f1f1db | -12.87767 | -50.14326 | 2025-11-20 01:11:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 0cff3be9-5e54-3d32-9583-4af7cb4cbe10 | -10.62571 | -65.2745 | 2025-11-20 01:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5b37460e-b7fb-3a3a-bccf-b6a410e7367a | -8.83307 | -62.30399 | 2025-11-20 01:11:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d0bbbfd-9cb7-3d9d-9e75-62f25f60f358 | -9.04168 | -61.94851 | 2025-11-20 01:11:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d87ed036-f77f-33ac-80c1-f25db501df1a | -11.33046 | -51.82133 | 2025-11-20 01:11:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 6051a4e0-82a2-35d3-82a6-526bcc3ff61f | -9.20689 | -62.34932 | 2025-11-20 01:11:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2591596d-35e5-3c2f-b81a-44b082894edc | -9.39295 | -54.60462 | 2025-11-20 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2f8a18e2-6914-3f1b-a11f-f0bf37ccaa0a | -9.39445 | -54.61014 | 2025-11-20 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0d98c82b-5b1e-30a3-bae5-7174c8dc0fe6 | -10.88706 | -54.13739 | 2025-11-20 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c8c33aab-3785-3c4f-b205-877b622a6305 | -10.4602 | -57.48305 | 2025-11-20 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0bee95bf-cbdc-39d6-a336-20b5255966b0 | -10.84508 | -56.95468 | 2025-11-20 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 6e7db736-5571-33ab-83c7-3a696ff59230 | -10.83714 | -56.96632 | 2025-11-20 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9a045523-3581-358c-bb6f-3d6c6e0ab824 | -10.3544 | -48.88922 | 2025-11-20 01:11:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 8eee89f9-7cf7-30ea-8fbc-27756af73aa1 | -10.88707 | -54.14675 | 2025-11-20 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 66078545-3178-3601-a623-db66522304d8 | -10.84655 | -56.96484 | 2025-11-20 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| de6ece35-eb43-3843-99ba-1b436ee245ef | -10.83566 | -56.95611 | 2025-11-20 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a6fb4dbe-e6f2-3379-ab54-b5a10bfed2c5 | -11.33728 | -51.82581 | 2025-11-20 01:11:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| abb9ed9d-aae8-3de7-84fc-699ed539cff6 | -10.5142 | -58.5801 | 2025-11-20 01:11:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d2f4ccd-2b68-389a-8d22-d8b7ca16fec8 | -9.04306 | -61.95877 | 2025-11-20 01:11:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7f4ab8c9-3804-3f75-9966-cec02feabad0 | -10.36197 | -48.93093 | 2025-11-20 01:11:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2db45caa-bc8c-3d0e-9160-b1f8e34aead6 | -12.88267 | -50.17216 | 2025-11-20 01:11:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 31398009-0ae7-3c6c-8eda-e7d7727e56dd | -12.88056 | -50.167 | 2025-11-20 01:11:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| f4f85cd0-356e-3ab0-946b-b290e325fcb3 | -10.35314 | -48.89685 | 2025-11-20 01:11:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 6ac60458-3f00-30ab-b2fd-5175aefe8db8 | 2.42601 | -60.98954 | 2025-11-20 01:15:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44a78f83-5fb1-3b34-b1ff-205f606fbaf4 | 2.41583 | -60.99734 | 2025-11-20 01:15:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 483ad4b4-50e8-3062-ba87-880402e8b770 | 2.42477 | -60.99858 | 2025-11-20 01:15:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0fd0333d-2d52-3f5d-80a5-b5d83eacf04d | 2.41706 | -60.9883 | 2025-11-20 01:15:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 46415a92-e652-3211-913d-65542aeff9f0 | -3.4389 | -50.1738 | 2025-11-20 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 07ccda06-1cdc-33f6-9ce7-fb9bbe10dc99 | -20.2967 | -50.9581 | 2025-11-20 01:40:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 246.7 |
| d8c691c0-96b3-3a71-ae02-024a14a4adb9 | -6.5631 | -51.1126 | 2025-11-20 01:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5d481f98-4bb7-3999-9bae-13edbf05d4b6 | -20.2962 | -50.9806 | 2025-11-20 01:40:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.6 |
| 81553f8a-640b-372e-a13d-b17b2669c917 | -10.3725 | -48.9153 | 2025-11-20 01:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d30385ea-9f03-3d6f-b04b-7dea1e3019ac | -10.3728 | -48.8936 | 2025-11-20 01:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9d017483-f669-3b13-bff6-ba65570814f1 | -20.3165 | -50.9766 | 2025-11-20 01:40:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 4971b324-9960-3ec0-8550-606060b4cb0e | -10.8401 | -56.959 | 2025-11-20 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| f7e372cf-6f89-3f95-911f-505d30ffb84a | -3.4388 | -50.1948 | 2025-11-20 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3892cd24-714c-3052-acce-907887341ca9 | -10.3538 | -48.8957 | 2025-11-20 01:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 47cfdb3b-456a-3792-a4a1-e39d73d20d45 | -10.3535 | -48.9174 | 2025-11-20 01:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 74315574-9eec-3b1b-80ce-522ed5deba71 | -20.3171 | -50.9541 | 2025-11-20 01:40:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 570f052b-3f7d-3e5f-a531-27cdbabf3759 | -4.0863 | -50.0654 | 2025-11-20 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 86a54dd5-d6be-33e6-bc95-83c6024029b3 | -4.1048 | -50.0647 | 2025-11-20 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c75e3014-a896-3e06-a7c9-4bf08a8c122e | -20.3078 | -51.017601 | 2025-11-20 01:53:00 | METOP-C | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c62ab0ba-d84b-3490-a7ec-fc148e770a63 | -17.6164 | -54.1936 | 2025-11-20 01:53:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 39386998-44d8-3012-8fdb-2c02c528274b | -20.7391 | -55.709 | 2025-11-20 01:53:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a20fda60-e5da-3c7c-ba12-afdae86fe9eb | -10.8362 | -56.967098 | 2025-11-20 01:53:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0942f4bf-ccef-3eee-8f6b-609887cec9da | -10.8459 | -56.9645 | 2025-11-20 01:53:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1b8c711-dee9-36c2-8f2a-05da4afc4cc0 | -20.298401 | -50.986198 | 2025-11-20 01:53:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57e884e6-d9a8-3f88-8713-cf891be9ecb4 | -20.2889 | -50.9548 | 2025-11-20 01:53:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bf09e30-ac87-3953-ab2f-fc747f46e6d5 | -20.3078 | -50.983002 | 2025-11-20 01:53:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c504763-4b2d-3d73-ac5a-61303f2151ce | -10.8313 | -56.948299 | 2025-11-20 01:53:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60789ed1-6c3a-351d-99b5-f47838e1cfd0 | -10.6191 | -65.277298 | 2025-11-20 01:53:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d386d7e-a41b-3e6b-bbe2-dfa1792d892a | -20.2889 | -50.989399 | 2025-11-20 01:53:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8454d194-4115-376a-a318-39c2b57c5a01 | -20.2983 | -50.9515 | 2025-11-20 01:53:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a415cdf9-0d4e-3337-b468-15fc70084406 | -7.3836 | -35.26169 | 2025-11-20 02:51:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a09ba23d-4713-382c-b67d-5b66fe0fe96a | -7.3819 | -35.26395 | 2025-11-20 02:51:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cda0c079-7094-3826-afa0-c034537b3a9b | -7.37533 | -35.26285 | 2025-11-20 02:51:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 25fd3ae0-d806-33da-a9f3-54e6d17b4b8e | -7.37703 | -35.26056 | 2025-11-20 02:51:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4b4f8913-73d7-3e7f-9f1b-a16428e53ae2 | -20.2967 | -50.9581 | 2025-11-20 03:10:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.8 |
| b48d7210-9c60-38c4-a6b1-23bcd808d4fe | -10.3535 | -48.9174 | 2025-11-20 03:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d2d6cb2c-e876-3bff-a20f-7250db5eb7fa | 3.1093 | -60.784 | 2025-11-20 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 60962b3b-5dbc-33e5-aad2-ce41bbd7e742 | -20.2962 | -50.9806 | 2025-11-20 03:10:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 176.7 |
| fad5833d-f858-3c66-aa11-09f48ef65317 | -20.3171 | -50.9541 | 2025-11-20 03:10:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 32cb7f09-60be-32e5-ab7f-b2d3ac78c0cb | -2.5053 | -47.812 | 2025-11-20 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9d985402-ba5b-3874-843c-104a1abea2f8 | -20.2758 | -50.9846 | 2025-11-20 03:10:00 | GOES-19 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| efb7e972-b0ff-395a-a902-a9ef66a26ca4 | -15.5389 | -50.6688 | 2025-11-20 03:10:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| cb7e3471-31c9-34a2-bbcf-57a0f3521dad | 3.1094 | -60.765 | 2025-11-20 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 26485ca0-2eb9-3dc7-a636-251db1309e57 | -10.3725 | -48.9153 | 2025-11-20 03:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d9376738-850f-38dc-835a-8c200ec3513c | -10.3538 | -48.8957 | 2025-11-20 03:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 6de788eb-d8a0-37db-9b22-1ad088eee177 | -10.8401 | -56.959 | 2025-11-20 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a61bd314-bfeb-3c61-a06b-00076c151363 | -10.3728 | -48.8936 | 2025-11-20 03:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 6715dc47-9b97-3239-a54a-14b71b5a9002 | -4.6689 | -43.226 | 2025-11-20 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5553707b-ca52-3025-b942-733d90438cc8 | -3.56007 | -43.47904 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 913e987b-cdd2-398f-af03-2d6d20c6002d | -3.29756 | -40.00781 | 2025-11-20 03:40:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30db738d-327b-3669-a09e-235285f696f2 | -3.34481 | -44.50993 | 2025-11-20 03:40:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4ce9802-3e49-3ddf-97a3-5920fedd4cac | -2.51235 | -47.81037 | 2025-11-20 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe00302c-aeb0-3b3a-8f6d-7a2f9ad49cdc | -3.55887 | -43.48129 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 12e1ddb5-ed3f-333f-b825-2965712af547 | -3.2349 | -44.8455 | 2025-11-20 03:40:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a22a7e-242d-3824-938c-9b20f78e6800 | -2.95926 | -41.55415 | 2025-11-20 03:40:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a05d96a-3895-3093-8811-fda6600c311b | -3.49866 | -40.29176 | 2025-11-20 03:40:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 48a23b14-7945-3ac8-a772-2f8eab7e60c7 | -3.7466 | -40.98481 | 2025-11-20 03:40:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33e0f4ac-c397-3a74-8707-b236b395dfc7 | -3.23278 | -44.85786 | 2025-11-20 03:40:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3667fb-c8ff-33a3-9bb8-4418d057419c | -3.5606 | -43.47575 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f75a6d4-c195-3791-b962-eac37f55246f | -3.23349 | -44.85374 | 2025-11-20 03:40:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc43aff1-b81c-3570-9fbb-d2521ffff090 | -3.66119 | -40.90228 | 2025-11-20 03:40:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
