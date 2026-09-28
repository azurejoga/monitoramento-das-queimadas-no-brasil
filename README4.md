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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0293b9eb-822d-35c2-8e49-1ce0a74240f1 | -10.826 | -57.2229 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16f4a574-b97c-3391-9597-edd2a395054f | -2.2692 | -57.014198 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d273d3d-9283-35c0-b420-8d83cbe0b72c | -12.6329 | -47.329201 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4d4e58-c1af-37dc-916e-e5c1d67230d2 | -11.04 | -54.044102 | 2026-09-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 137deb3a-1d66-384a-a676-400e1e82cae1 | -10.6541 | -58.771 | 2026-09-28 00:33:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddabce43-b042-3b6a-a060-551451920daf | -3.203 | -51.052399 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8093a9fe-427a-3720-83d6-3eec4d83d185 | -3.2254 | -54.323399 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1172097d-6d30-3b25-9f81-a3237f6074fa | -7.8227 | -55.134899 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e749873-32e4-384a-90fa-919bb894540d | -2.9923 | -54.747799 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f23ddc-7f13-3633-82b5-84e83ecf6fdb | -11.01 | -54.1394 | 2026-09-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08272bd9-bcee-3e26-a3e6-dff0a7814406 | -7.7188 | -54.7663 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac20256f-167d-3315-a964-194abdec2800 | -13.7161 | -48.815498 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff7c0e40-76d7-34b0-8d76-2ef46c73c098 | -2.6713 | -56.4674 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20a19c68-88b0-349e-8518-ea20d5402db9 | -7.709 | -54.768501 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb87a76-54fe-3bad-80c5-d0c855f72fcf | -14.5253 | -48.319698 | 2026-09-28 00:33:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0cff9a56-3e60-35b5-a0e2-aac9c0125ad9 | -10.8747 | -43.6866 | 2026-09-28 00:33:00 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0a2e9b6-e791-31d2-8191-f84d1500c0eb | -13.9854 | -53.989498 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25dfe3b9-4f23-361a-85d2-194c89f61d25 | -22.350599 | -46.9627 | 2026-09-28 00:33:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9aef081a-c9fa-34db-9174-3cdc53a8c5e7 | -8.0372 | -54.897999 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570c687f-e3c4-3723-96d6-32f177d16f4b | -8.352 | -45.4496 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 351b683f-e2e5-3af9-a78d-718d6f823092 | -10.4147 | -53.833 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a06789ce-ede8-3479-b532-42ee384f37c0 | -2.91 | -54.115898 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff652c2-97c3-30a4-8c13-2fcd494889cf | -2.9206 | -58.305698 | 2026-09-28 00:33:00 | METOP-B | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 492b9df7-0d4c-3697-a42d-a9551de12ec1 | -2.6682 | -56.4538 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3eca584-7d0a-3eb3-99e2-9a6de7754cc0 | -11.1834 | -44.819401 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e34a05d8-8176-330c-ba49-d8a3a36d6fdb | -3.0816 | -58.014 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78a0b276-faa9-36be-8136-f1ee06612f59 | -16.464701 | -55.0793 | 2026-09-28 00:33:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2287a8cb-d7d3-3699-8765-67fac4e5373d | -1.8146 | -57.1007 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c863b366-0ed9-3a7c-b407-00e947d49c1e | -9.4936 | -46.382301 | 2026-09-28 00:33:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 691e577b-4839-3c1d-97c4-08e19bd8a0c0 | -9.5313 | -63.5532 | 2026-09-28 00:33:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d891c1d-363b-315d-ae9a-ac16985fca6d | -21.0228 | -47.261902 | 2026-09-28 00:33:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e366129c-efce-3255-9593-b2e6d8f874f9 | -11.2065 | -44.789501 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53667a6e-596b-3fed-ba17-fc9797a4d9bf | -11.0912 | -51.314201 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3b9da4f-e099-33ed-b56c-c409332cabe0 | -11.3562 | -43.409 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f258057-3bf2-3eb7-b96a-23bdd7384501 | -10.2177 | -49.987999 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6526287-d72a-3df7-9f13-e07b54ed8788 | -9.9938 | -50.130299 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c56d6ac9-3ed1-3077-9d9f-d846c4352fd9 | -12.6318 | -47.2841 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6d3160e-fee1-35a0-8696-88d4eaa79ae4 | -10.8818 | -43.7131 | 2026-09-28 00:33:00 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5837b7a-15b4-35df-980e-ce2b20c0a267 | -2.9118 | -54.1236 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1445df6a-1806-3b70-8d50-ee25de1fd202 | -11.7744 | -51.057598 | 2026-09-28 00:33:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48233e88-78e2-3e1a-bb43-3bdb1344ea28 | -12.2053 | -50.3918 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2766340-2f9e-3896-8074-42ddbe3ee54d | -2.5522 | -58.041302 | 2026-09-28 00:33:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8def587-aa96-3ff3-aabd-e9aaa33c2d0e | -2.7818 | -57.688099 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc655969-0114-3ea0-89f4-637c76906c55 | -11.0933 | -51.3228 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2b1a48-dc8e-36e4-909f-137c2c9b521c | -22.4562 | -48.588299 | 2026-09-28 00:33:00 | METOP-B | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f39f9599-08d9-3803-bc84-8b1060db375c | -13.9771 | -53.998699 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 240d3e45-b95a-33fd-bb6c-28e2c582b7c4 | 1.6509 | -55.903999 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07f9aee-b7e4-3126-b44e-b6b17aaa437a | -6.6717 | -45.6619 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 113e1ec2-7712-3acc-bb2b-afe9aa3bab3c | -6.3036 | -56.030899 | 2026-09-28 00:33:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf9c6a1-2689-3096-83a1-8b8db4274bfd | 1.6788 | -55.962898 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d3bf04-1751-3744-9a9e-701d56dd087a | -11.9618 | -49.296501 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 989504d8-59fd-3f39-8a50-579676779a73 | -7.6878 | -54.765999 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c67ea1ad-ca97-3d20-84d2-4e24d341434d | -11.2219 | -44.808998 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82b966a3-f61a-3aca-9fba-ea24be1d974c | -11.0214 | -54.1441 | 2026-09-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43ff130d-64f6-3696-befe-27e06c9540e8 | -2.9324 | -56.573799 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee6fee0-2ecd-315e-8cca-e9cdb8baded1 | -12.3057 | -46.406502 | 2026-09-28 00:33:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc649e1f-7ed6-368a-bc6f-43c5ba901442 | -12.6185 | -47.2724 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9f9f7e-8472-359c-8a56-ab338ce44279 | -12.1528 | -50.3456 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc40bd3a-324b-37f5-9caf-6de10d9f65bd | -11.3658 | -43.406399 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad247158-63da-324c-9c54-a0c3bd145a16 | -13.6967 | -48.820599 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be4c4644-bf37-3324-9d57-d86fb55d85f3 | -10.8209 | -57.1996 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1518b9f4-a314-3165-b9c6-be39ec606188 | -11.0973 | -51.339901 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae249f3-bbce-3f88-9440-14cc08b3d491 | -3.2102 | -51.039001 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87534c90-4694-3bc2-9760-437f462b0e76 | -9.9962 | -50.140499 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdbf2aa-83b0-3ac0-9c9a-7a5be7eb5405 | -11.7063 | -44.533798 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eeb26416-ad41-3fa9-9c7a-cf6f892ccea3 | -12.6706 | -45.023102 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 138107f7-3bcd-3f6c-bbef-e752d87f62c9 | -11.7026 | -44.558899 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef64a1db-c5a0-38e6-a682-b55557605fa6 | -11.1872 | -44.794701 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9d2c66e-6491-30b1-9f2f-14e9ca42fb9e | -12.6856 | -45.0406 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 469a27ba-b954-3f89-8acf-0171d6389a76 | -11.1349 | -50.064602 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bcafefe-e3b3-3ab4-970e-6dddd15e7daf | -11.1324 | -50.054501 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c4060ba-fc64-3293-9314-0e28650089c6 | -2.6569 | -56.4491 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51593ce-b1f4-3cff-884b-ff89fdfaafe9 | 1.6575 | -55.920502 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebea43c-6b36-3bf9-878b-c89c2094d930 | -4.0348 | -54.211399 | 2026-09-28 00:33:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9805f5a8-d0e8-33ab-86cd-039fd62d4b6d | -4.0383 | -54.226299 | 2026-09-28 00:33:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ca0e87-a9f7-31e2-a0a7-96781087ef9a | -9.9841 | -50.1759 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc6654c8-9678-3ae4-b09b-8ff9897bc747 | -2.9309 | -56.567001 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8030bda5-e124-3db2-8deb-d0ff672b0f0e | -8.2324 | -45.504101 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa7aad06-e20a-3bbe-8730-68d3d11c1700 | -2.6629 | -51.740299 | 2026-09-28 00:33:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ededc1-cf3b-32a7-94b3-078cef95494b | -9.3222 | -45.384602 | 2026-09-28 00:33:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77c904a8-a668-3ce4-8d63-79b036ec2c53 | -4.0481 | -54.224098 | 2026-09-28 00:33:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f094a872-1786-350d-93d7-d8abdb6ca1b8 | -6.6475 | -55.0886 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef1e7b75-5c84-385b-9cd5-361f1a1ea555 | -10.8193 | -57.191898 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89ab8c67-cf68-3dba-89ba-4e36b233a911 | -10.4017 | -53.821098 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9626d8-bf15-3554-8c6c-23a6742dda0d | -6.6604 | -55.100101 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01d0c00-e9c9-3b35-93b8-8d70c2ef7e25 | -14.4821 | -53.629501 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1b18ea1-9822-3c2b-a377-d1ba93f8fdcd | -13.9838 | -53.982399 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03e62643-ab4f-3ed5-9b95-e0735b1963f2 | -11.687 | -44.539101 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 937ed79e-c26e-30d7-9724-5155c05e00de | -12.6221 | -47.286701 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4270b222-3745-31eb-b756-37969367414b | -6.692 | -45.9897 | 2026-09-28 00:33:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0b5cb2b-eac8-3c7e-a820-7ce58e01a647 | -18.092501 | -44.376499 | 2026-09-28 00:33:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab620045-27e4-3877-af93-6e0664336df7 | -3.0047 | -54.214802 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa9a93e2-b007-3f46-bc9d-30ec2f340c50 | -15.4111 | -47.9254 | 2026-09-28 00:33:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa72681e-9536-3a14-a83f-4d851676219e | -2.6572 | -56.542 | 2026-09-28 00:33:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca4f6f81-596e-3f2b-ae15-e79fb0851831 | 4.3465 | -60.705101 | 2026-09-28 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7f55c7-b3ad-3b41-bf2f-f188de8fce4c | -6.6891 | -45.608501 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e86ce4d4-86aa-32c4-888c-10f81f5af136 | -3.357 | -50.477699 | 2026-09-28 00:33:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ebb290-d03a-3b75-8f6e-ed13fa1d4125 | -11.103 | -51.3204 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0438a736-0704-3067-8fda-b0de99493044 | -13.9787 | -54.005699 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f46d18d0-0292-3caa-9414-18d317033812 | -12.7334 | -47.317799 | 2026-09-28 00:33:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
