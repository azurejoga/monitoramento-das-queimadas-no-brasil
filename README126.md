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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d44d5806-29ed-35ea-8eca-c35f46e82c58 | -13.8957 | -45.4681 | 2026-09-22 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| e8d89985-751c-3571-a231-bd2788ffcaf0 | -6.2396 | -41.6634 | 2026-09-22 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 189.8 |
| 55602da4-bff8-3e12-8c89-9e603b49aeff | -8.8105 | -44.2757 | 2026-09-22 13:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| d9a96638-7a5f-383f-9296-7e2edfc41cc4 | -13.8952 | -45.4913 | 2026-09-22 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| ecd71699-902e-324c-acc5-4181384bbe67 | -12.4588 | -47.0173 | 2026-09-22 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0dced979-604a-3fdb-93c0-51b1777fee25 | -13.8729 | -51.848 | 2026-09-22 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 153.1 |
| a8d7b807-3707-309a-bff2-23589a0676c3 | -10.6094 | -53.9902 | 2026-09-22 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1b4c10ab-7c18-3e2b-a387-559aad920e10 | -11.156 | -51.1051 | 2026-09-22 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 732aa346-cdb5-366a-8635-0e174eab1251 | -9.6298 | -43.9453 | 2026-09-22 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 99c82fbd-13e7-3958-a519-f97d43fcaad8 | -8.3965 | -45.6244 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ce5cd992-edbb-3da5-8691-8c413b092367 | -12.8906 | -50.9267 | 2026-09-22 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 5a304b2e-4342-3d0b-b236-493f3c49ccfb | -12.6796 | -50.974 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| dc99912f-5843-3f36-83ea-ac7d1da880eb | -10.5748 | -46.7296 | 2026-09-22 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 243f0ce8-2b9e-3fc6-b118-dcf9669134da | -12.3018 | -50.7203 | 2026-09-22 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9405d75f-5e68-30e2-957b-c9fbe7429a46 | -12.283 | -50.7011 | 2026-09-22 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0912077f-e07f-36c0-bd60-56040882b183 | -6.9414 | -42.907 | 2026-09-22 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 43d4d8f6-003e-3613-a50a-1d0fc63b6394 | -13.9146 | -45.488 | 2026-09-22 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| f8fd2d53-0aa7-3efe-b4bb-792e825e10e9 | -6.9416 | -42.8834 | 2026-09-22 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 948fb5cf-8c13-3ee8-be59-3e80880cc4dd | -12.3025 | -50.6774 | 2026-09-22 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| e943117e-557e-3953-9a45-805b70cdad18 | -14.6878 | -45.6762 | 2026-09-22 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 7c8a1fdb-7e79-3a74-a44d-edc5aea8d607 | -9.9163 | -45.0885 | 2026-09-22 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 37ee8a6e-4693-3aa4-9542-4454d300c2b3 | -3.7129 | -60.5832 | 2026-09-22 13:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a50619bb-7c1e-39aa-9d26-d8c5f6d28a49 | -3.8039 | -60.7521 | 2026-09-22 13:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3a971aa9-12c4-3d2d-aa83-070da55d94e2 | -7.4953 | -45.4855 | 2026-09-22 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c3cfb6e1-4069-3a92-b8b6-c592317039ac | -9.9064 | -48.443 | 2026-09-22 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 8d2ab4e4-5d6a-3a0f-a160-81b5534a4125 | -7.0352 | -44.6396 | 2026-09-22 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 93d95439-6bf1-33ea-b1a6-97b497ed1202 | -10.4536 | -51.325 | 2026-09-22 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 29593214-9d8d-3c1a-bd2a-cef7cdc060be | -11.4404 | -47.3355 | 2026-09-22 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 29327511-337e-3ed3-9ede-41001633a045 | -12.4196 | -47.0679 | 2026-09-22 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 704c2119-793c-3d43-96e9-6a99fb22d52a | -6.6699 | -59.9251 | 2026-09-22 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9b621628-c323-3eb4-af9f-f06c299f27f5 | -9.9061 | -48.4649 | 2026-09-22 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| f650ce62-c020-3452-94f2-c64fffa2a065 | -13.2225 | -51.717 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 82fbf13a-612d-3e52-a525-310c27e4ab84 | -12.6987 | -50.9717 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| aaece404-9d2b-3796-90dd-65065ae420c9 | -8.7912 | -44.301 | 2026-09-22 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| cc882146-b165-357f-a396-544fe26bd644 | -12.3021 | -50.6988 | 2026-09-22 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| d511483e-eecc-3b2b-b7ec-40e9158c5521 | -11.3229 | -51.3626 | 2026-09-22 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8857ec8f-be85-3471-bdf0-d069e99d5da6 | -11.44 | -47.3579 | 2026-09-22 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3b5e4a7f-7618-3665-bec7-4b2ddcfbff0f | -9.2951 | -46.1606 | 2026-09-22 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 57096e2d-b9b3-3993-8507-2772eb5d560f | -11.1563 | -51.0839 | 2026-09-22 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 82f598b5-5b35-3fb0-9fb0-d5b8c8ca1dc8 | -6.6515 | -59.9258 | 2026-09-22 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 0fdf903c-6450-349a-aeba-726a70adc70c | -12.3484 | -50.1779 | 2026-09-22 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b4a02d4d-f6c8-3263-9aaf-9da4fd5165b6 | -11.024 | -53.9943 | 2026-09-22 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 724b5e9f-1684-38b1-8297-c05764241f9a | -6.6331 | -59.9265 | 2026-09-22 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 63defedf-cf3e-378f-9fc6-c12f61e60b2a | -6.6514 | -59.945 | 2026-09-22 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2a933ca2-5649-3971-afbf-2028e652cb47 | -6.6332 | -59.9073 | 2026-09-22 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 97e1e2d2-ad2d-3f4c-b6c9-ae1cc93a3d20 | -11.175 | -51.1031 | 2026-09-22 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 203.3 |
| a8c209b5-9034-3b98-a918-0354044f6722 | -11.0052 | -53.996 | 2026-09-22 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 73030bc4-2b69-3cd1-9b35-5bffc7949352 | -5.6411 | -43.3687 | 2026-09-22 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ef9fb34e-01ef-397c-8250-eaf6964c6af9 | -9.2948 | -46.1831 | 2026-09-22 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f2547e40-94a4-31e7-911b-f3624e2c17bc | -6.2585 | -41.6617 | 2026-09-22 13:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 73c339b6-810a-3307-b305-36836bee0000 | -9.8869 | -48.4887 | 2026-09-22 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 36a08c76-d8a2-3bf1-9676-010d776184af | -7.0349 | -44.6625 | 2026-09-22 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 78acb9dd-736a-3ac7-88ee-eea223725c62 | -3.4781 | -59.5396 | 2026-09-22 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 385621e5-3ef1-358d-9eb8-8c9d5cee8250 | -11.4113 | -46.7798 | 2026-09-22 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 278.2 |
| 35a23435-7469-3b07-a089-32396d14d26f | -9.5833 | -45.8345 | 2026-09-22 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 7705893d-9925-3dbb-b170-620cfda26fe1 | -11.4213 | -47.338 | 2026-09-22 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 35d557b8-8873-3e15-9ea2-5ecb47fd91a8 | -6.6146 | -59.9272 | 2026-09-22 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 6f772528-a4c3-3324-8b0c-6869b6ff0667 | -11.3413 | -51.4029 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8fbbdfba-a4bb-3799-92a8-adbfc5d0aa6a | -13.8952 | -45.4913 | 2026-09-22 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| a60efb50-8862-3d4c-a475-8b417108c8e4 | -6.7989 | -43.9008 | 2026-09-22 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fb436b3a-dbf1-3c20-9ffa-9b177ee6709f | -6.633 | -59.9457 | 2026-09-22 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 27aa4a26-c937-379e-b77d-4979eba7ced6 | -11.3232 | -51.3414 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c22890c2-9922-3364-ab9e-32c7542dd82d | -7.0352 | -44.6396 | 2026-09-22 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 6a587a0c-395a-3176-adf3-61a9f8a133d7 | -7.146 | -48.4352 | 2026-09-22 13:10:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e484fbd4-8ce5-3ced-914c-268b87b22b8a | -11.4404 | -47.3355 | 2026-09-22 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8807682d-c5be-3605-bd3a-250c75518f40 | -12.2834 | -50.6797 | 2026-09-22 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 23a9b37a-e618-3327-9389-5f6d12d92641 | -10.6094 | -53.9902 | 2026-09-22 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 9e493975-7b79-324b-9a53-8f9fb838e7e0 | -9.0276 | -44.9875 | 2026-09-22 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5b2dd142-92e5-3eeb-8586-85349d56e1b8 | -3.4781 | -59.5588 | 2026-09-22 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a155b65d-b4a2-365c-9ffd-a5fd3daf45dd | -14.6878 | -45.6762 | 2026-09-22 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| c0ddb3e1-301a-31b8-bb05-e438392bdd0d | -6.4485 | -59.9909 | 2026-09-22 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eac167e1-a72f-3909-9525-eabe9f7c7193 | -10.5906 | -53.9918 | 2026-09-22 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 914a8633-8db4-35c3-8519-65be2ed60faf | -9.9064 | -48.443 | 2026-09-22 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 479d1e1b-0278-3e8b-8d7a-6e7fce51eefc | -11.024 | -53.9943 | 2026-09-22 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ce35d0e0-d00b-3bd0-a22e-3369c3141dc2 | -3.7856 | -60.7525 | 2026-09-22 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2bf3d08c-7692-3321-9fe8-68a6ef782b7f | -3.405 | -59.522 | 2026-09-22 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| aa576387-11e1-36ad-bae2-7642a7d89daf | -3.6398 | -60.5846 | 2026-09-22 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 055fdc64-3c55-3c0d-916d-5e930e4bcb39 | -8.8105 | -44.2757 | 2026-09-22 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8f6b04a3-935c-3ebf-954e-858f6b96d8fd | -6.7354 | -55.3074 | 2026-09-22 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0daa29c3-3c87-3f18-9012-5cfa121c89bd | -11.3606 | -51.3797 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b10f06c4-7dd3-3fd0-a911-c3da264f0e29 | -12.0836 | -50.0378 | 2026-09-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 457f21a3-7e73-39dd-800e-80966aba2874 | -11.4109 | -46.8023 | 2026-09-22 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 924221e8-32a4-34d5-a183-42fc715e62b4 | -12.3484 | -50.1779 | 2026-09-22 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5c42df6d-81d8-31e8-8cf3-14c6c40ebf0a | -6.2165 | -45.9518 | 2026-09-22 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 824bed0d-71f2-36c0-bce3-292ec0fbf482 | -11.3922 | -46.7824 | 2026-09-22 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 7afcbdf3-8539-3aca-8dc0-78cee2ab6ae6 | -12.6796 | -50.974 | 2026-09-22 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 38873f7e-5679-3f38-ae99-9bca570f1865 | -6.9416 | -42.8834 | 2026-09-22 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.8 |
| a1d83c3d-06de-3444-9cbd-6c97dba5ae85 | -9.2759 | -46.1852 | 2026-09-22 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.1 |
| d714a9bb-8cd7-33f8-b8f7-0e11309034f3 | -8.7912 | -44.301 | 2026-09-22 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 4989e960-9b91-3065-b715-5e46fa6917ca | -3.4599 | -59.54 | 2026-09-22 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 28511682-2665-3a09-a536-bd54b2613939 | -12.3021 | -50.6988 | 2026-09-22 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 6d7e445e-4216-35e6-9a60-d9216bbdb328 | -3.3867 | -59.5223 | 2026-09-22 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 11ffab12-e3e4-379a-a70e-f698dbad130e | -11.6891 | -50.9619 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9564057e-4961-35d4-8d7b-c3d968f0f6f6 | -7.1203 | -43.7323 | 2026-09-22 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 24321e4a-1950-3751-b9b5-9c9cbbfe654c | -9.257 | -46.1873 | 2026-09-22 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 35d1b808-0ac6-3cc0-9cf4-1ac43a29f097 | -11.3229 | -51.3626 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6407860a-1324-3ad5-970b-77739f191330 | -8.6171 | -54.6126 | 2026-09-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f18fc3b5-6980-3608-8ece-05af3b58a20c | -9.6108 | -43.9477 | 2026-09-22 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 3904dbc7-8c1e-3be8-8dc2-5c374a2584ee | -10.6878 | -50.751 | 2026-09-22 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| ddf71229-0e33-3088-9d40-d24025c3f13a | -11.3416 | -51.3817 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |


[Clique aqui para ver as próximas entradas](README127.md)
