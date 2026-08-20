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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e633ed15-fbb5-3ae2-a61c-a9653a0df3b6 | -6.38088 | -54.94754 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c34ab69-98cd-3ae7-b2c1-dc1f8dcfa509 | -8.47189 | -46.96172 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 588f18db-56d4-320c-adf8-741aa07cf59e | -6.31526 | -55.91868 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9574f0c-69b9-3da1-bf4d-9a4bd870351c | -6.38475 | -54.94453 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8aa1cfe-8bc4-3ecf-8fa6-596502e7f512 | -4.27391 | -55.5759 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52e448fa-8876-38cb-9241-951f770e9978 | -6.01886 | -57.87125 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9be81954-0d01-3ced-af05-56e1e9d19934 | -6.38916 | -54.93801 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44103edd-f746-39d2-bff3-bc57da3d7224 | -6.94062 | -52.78289 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b4c4692-c799-32f8-9bf7-17ef8067212c | -2.87458 | -59.22676 | 2026-08-20 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2e2cf6d-2975-3161-a439-77344a0af5b8 | -2.87437 | -59.22434 | 2026-08-20 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b201fcee-50c0-38b4-b96a-7382ca4d5d35 | -4.50785 | -55.4501 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 948b77d2-8ca6-37f4-ba3e-18022a9a6b30 | -6.70971 | -59.10391 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3456691a-5bd9-3fd3-a557-f2cafce49b40 | -6.27115 | -43.2784 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0cb4aeb-53a7-36ef-8858-46ed384f41ee | -6.59231 | -58.96353 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f25f48f5-5d72-3788-9eaf-ee108b36be8b | -6.0887 | -57.91656 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c7c1e22-657f-3f7c-9160-ed1c01869ecd | -6.58475 | -58.98773 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95c7aabd-e665-3e1e-9fcf-581bb5efc49b | -6.10371 | -55.81434 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9aa7fd97-3f76-3e3f-bee5-b91267af233d | -6.70389 | -59.09439 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a08a0690-e97b-3472-a4de-8fd4aecbd259 | -6.23044 | -55.61195 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c728b406-94bc-39b8-9f22-c4fc308b05aa | -6.69668 | -59.09324 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2cb6b7-c3dd-3e96-a4c9-1f4bcbf31fd8 | -4.44053 | -55.37967 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b110d35c-76c0-3ccf-83df-945fa7f9e096 | -6.69823 | -59.10629 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ecfee9c-2342-3c64-a2c6-7111ba828b02 | -6.70816 | -59.09088 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3814bf8-b410-3909-b3cf-f29f0ec98078 | -1.83752 | -54.4934 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7826911-76f2-37ce-a9fe-716e8a6587e3 | -6.34436 | -54.89888 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d45d9b0-ba77-31a0-85e6-c2dfc8308741 | -6.58382 | -58.97062 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 238ab7f1-cb76-3ee0-a625-cf8fcf413bf1 | -2.82866 | -48.65018 | 2026-08-20 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 280bdb1a-9882-3a6a-aa87-494b07723818 | -6.14267 | -57.86367 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17acf70-7c9a-3d65-9072-749bc2a03221 | -5.81742 | -56.31851 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a406eb2-ae90-39a3-af0e-61ad35a41bb5 | -4.09205 | -42.50343 | 2026-08-20 05:04:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de48af79-6bc4-3476-bacd-46541b6f8e4e | -3.10395 | -61.21172 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b74172-23b8-32a8-b93b-809e82aa79a1 | -6.69172 | -59.10091 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8301bfce-a6ce-3894-9dac-f88c92824da8 | -5.79695 | -55.7094 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf4411d-cd4d-325f-8e7d-d2ff8fda234e | -6.89944 | -55.22217 | 2026-08-20 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 551b16e7-973a-390d-9def-49ea2b892db6 | -8.36762 | -46.3384 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d623b5d6-ae4b-3475-a786-971903a2c77d | -6.24068 | -55.41521 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933064e0-cd82-3da8-9d2b-17918bb72cea | -5.7354 | -43.27695 | 2026-08-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61d4fdcf-5790-3603-a154-3082261300c0 | -6.27191 | -43.27264 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 590d97bc-fe3f-30ee-9525-1a06d9ea0b57 | -6.14731 | -57.85674 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c0a8ea-7eb7-368b-9e6b-8b940f556b40 | -6.4873 | -50.55965 | 2026-08-20 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95fecc00-f376-3cac-a94b-6cedb3e5837f | -7.05084 | -56.52152 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4657a1ea-637a-3756-be7f-e30f5b421bfc | -6.7813 | -42.88994 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 65e8f8a4-c3e5-3448-8d1f-172adf1bbc7d | -4.95091 | -56.27031 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 975a2ab2-cd22-3bbd-b4d8-b40503773a26 | -6.08929 | -57.91281 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcb5bc3c-e138-312c-b2f3-b417b740c9d2 | -7.96586 | -44.6654 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d347743e-e6e1-3909-a6d1-0fdcbcae862b | -6.13766 | -47.22774 | 2026-08-20 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f03364d-e111-3b86-8b80-991f2799a9e8 | -7.74913 | -49.46655 | 2026-08-20 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c7a1332-a853-3c65-8e35-223e72208e6b | -7.34194 | -45.83245 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4e06106-a1a8-33d4-a529-35097c25d522 | -7.76655 | -49.20292 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9240a2e4-6517-3bc1-a47c-0b8b43b106f5 | -6.42592 | -56.19139 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134cdf07-0519-3e52-9a6a-153e70b6815e | -2.79269 | -49.52085 | 2026-08-20 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a299700-6372-3692-9f61-b660fecebc27 | -6.14327 | -57.85993 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e79d33-8d5e-363b-ba65-c29d46fe2694 | -6.24399 | -55.41572 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b8fa48-fb45-3d6e-b2dd-ecf619d46143 | -7.25082 | -49.88693 | 2026-08-20 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 515001f8-0a8e-3fc2-9bed-c51815fab463 | -7.45285 | -47.172 | 2026-08-20 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1914c0e-9954-377c-a3f7-0bba3cbd49ba | -6.44614 | -52.75757 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 233b3c9a-5463-361f-8416-df3fcfaedcab | -6.78142 | -42.87959 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6de96e77-55f4-3da8-8b5b-a6ea74ade58f | -6.44018 | -52.74818 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e350ff0-d8d4-363a-89c2-8750445fc71f | -6.70884 | -59.08678 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7beffc74-d647-3044-bf70-f88d063406c3 | -2.64191 | -47.98259 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96c6e663-e65b-3e36-b98e-a3c70aa19741 | -1.83475 | -54.48945 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1d97510-f56d-3e3a-8b9a-cd7d11623cd5 | -5.80195 | -55.72077 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd27f7c8-7b84-3917-bcc8-36cbfabdcd7e | -2.99726 | -51.24147 | 2026-08-20 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 173aef73-ed34-3b81-b9a1-202193493095 | -6.28954 | -43.63788 | 2026-08-20 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 491a2fb5-b390-3e4a-94e0-7389deed419b | -6.95939 | -56.41053 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a4accb-5e9b-3c9d-b3f6-4ddf04f83461 | -6.88976 | -56.44222 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95f2f475-5f93-3f8e-bd7d-2c6611fd300b | -6.39529 | -54.94255 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e3624d9-7c4d-35c0-9976-60bb287678a8 | -7.60019 | -45.17757 | 2026-08-20 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a1f792cc-2310-398b-b20d-ac6d0384de8f | -6.10049 | -57.86457 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfc8686e-2060-3efd-8180-c3e7cde9f9dc | -6.43719 | -52.74348 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6272ac9d-6cd0-32fc-b137-5c1ce7c7677f | -6.57066 | -51.21724 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79fd5c54-723c-3f7e-8a8a-600cfec2fda4 | -7.3439 | -45.82626 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9701e529-7206-34b0-a370-f4f161d68607 | -4.12739 | -49.44963 | 2026-08-20 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dafb9771-ce7b-3ae6-a3a5-6aa705ed11af | -6.61444 | -56.35573 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5eb0691-2fad-3ec4-84f8-3c1c170e2bc6 | -6.43907 | -52.73095 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 472f8e79-dcca-3455-a814-f41063aa6cb7 | -6.08406 | -57.9235 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8b62870-b945-38d9-9799-6ff0a2dfb055 | -6.70081 | -58.94255 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf254218-01ce-3a0f-bad6-71a25f1b885b | -4.51116 | -55.4506 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62927246-7f70-360c-a7e4-7651b2b5ba02 | -7.34877 | -45.82523 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1eb8684a-c352-350b-8dbf-270233af02f9 | -5.87067 | -57.67624 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ab77ae6-085b-30ba-88ac-b7f8ef322b92 | -5.80802 | -55.72525 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec89d4e6-72b9-3ce3-b9e6-e3f0b168c3e0 | -6.24345 | -55.41919 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7961cea1-87d5-3db9-89b8-b0e53047b45f | -6.71175 | -59.0915 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b0e23f2-95d6-35d5-a496-fe82544134e5 | -6.59947 | -58.96472 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebb9572-fc93-3d27-bac4-803fd6f24f3a | -2.64706 | -47.98595 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d279f6c1-8270-3031-9a10-c1e7cc4b33ed | -6.31472 | -55.92213 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 107bcbbf-75a9-3a66-8e63-7a58df75986c | -7.35397 | -45.83004 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e0036576-8bfe-3f14-909e-20981581c77f | -6.40637 | -54.93707 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba85f1d-ea31-34b6-8776-b1d66983312f | -7.34768 | -45.83326 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ca2fc15-b9d0-3655-9457-5fea9ed4e5ed | -2.64244 | -47.98523 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae3ad19e-02da-30a8-b1cb-1db16fae8fea | -3.96169 | -43.11271 | 2026-08-20 05:04:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e03608a3-920d-3bf4-a7be-ab53dc3ebe02 | -6.10333 | -57.86891 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b423759-9381-3a40-b68c-5ca6770878df | -6.71963 | -59.08855 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 516eeecf-8cde-3a37-856c-e84d29a1d035 | -7.02947 | -56.6143 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7170dbdc-9f13-3064-9b2a-6e56fbb8938d | -4.39245 | -55.4709 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be6fc49e-7b0b-3acb-9c4c-1edee898cabb | -8.46741 | -46.95399 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53905a08-32d2-372f-a87e-2263e0d4a253 | -7.34139 | -45.83646 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1a1a6b1-c421-3d7e-8928-f373d4ab3585 | -7.45329 | -47.16876 | 2026-08-20 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3341e89-cc9b-3347-b5bc-c1653b81c827 | -8.48273 | -46.9632 | 2026-08-20 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e21ff984-dc18-301d-b279-749847ed1b5c | -3.26005 | -61.16416 | 2026-08-20 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README43.md)
