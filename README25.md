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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7677b777-30fb-3ce8-99ea-37e3acab6fb0 | -11.6179 | -43.719501 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14cb61b6-32ff-3b9d-a5ee-db0a274fd1f4 | -7.1463 | -46.5798 | 2026-10-09 00:28:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f62ecd2d-5551-3c4a-b999-70785acd9f73 | -10.0413 | -48.2197 | 2026-10-09 00:28:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b031ae7f-50d5-399d-a450-df2b3b3cf0ef | -11.4607 | -43.3964 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2e98c43-eaea-33dc-a31d-31d1c2fa7c4c | -7.2221 | -55.087799 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 906c15e9-d8fe-3c51-a9ba-ca84f6593386 | -8.9908 | -47.737999 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccad9c63-3ab9-364c-bbf7-64ce2ebbaa58 | -2.881 | -54.157501 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0316021a-1507-3180-99c5-e119cc5d488a | -6.8926 | -45.917702 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 608be302-cdd7-3aff-80aa-835441e865d9 | -11.1763 | -45.312 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 842455ce-484f-3ac7-a3f9-14f2effdc984 | -16.9944 | -41.166901 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 538c06ac-3a83-3b5f-8fda-8e8f363e8473 | -11.848 | -43.598499 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce7840b-765a-393f-acf2-946f1c89589f | -5.284 | -47.9077 | 2026-10-09 00:28:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5395bb51-f070-336c-a7e4-e98e4032b74e | -16.961399 | -46.3536 | 2026-10-09 00:28:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a158e4a-fc95-3a9b-8916-c8f485bb86db | -8.9178 | -45.169899 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9411c6f7-a359-328b-8ab3-dc4647b92817 | -4.5293 | -49.671001 | 2026-10-09 00:28:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b644bba0-5c42-3f82-8a73-d3d70ebe2086 | -6.8977 | -45.894798 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b38d80b-a138-387b-a21c-e5a1b1fb1408 | -13.191 | -54.393398 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d20d0bb-fdd2-3957-b354-a562fb7c890b | -11.7125 | -43.637699 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea6a1531-88e2-31f4-a4ac-81bd2bfc4f2c | -3.2646 | -50.398701 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c43af5-aa34-3a9d-a02e-4c666b869177 | -5.682 | -53.4911 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccce2713-ee56-3858-a331-32acdd2d5ba5 | -9.91 | -44.863602 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf476cdf-0bca-3785-820b-ba07bce0a96c | -11.459 | -43.389198 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4566944a-3551-3a14-b75f-ced3e9750992 | -9.0254 | -44.379799 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 020fd2a2-1d12-385b-b50f-55c6306925b9 | -4.9403 | -45.724098 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82f6a14f-6245-39ba-9d80-e59a69b8bbea | -11.6228 | -43.606499 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c393e465-90fd-318d-a3b0-1975d2acb981 | -3.3033 | -53.716999 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60597464-299c-33e9-ac74-35e3a4887e50 | -5.2742 | -47.909901 | 2026-10-09 00:28:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e791eeb6-2100-3c71-abdb-8626d1a86429 | -6.6803 | -44.3241 | 2026-10-09 00:28:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6897e98f-0897-302d-a3cc-c16684dd2bd3 | -5.3876 | -44.178699 | 2026-10-09 00:28:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f678fe75-a8e6-3d3e-8a6e-de76cefe4dd3 | -13.3591 | -43.890202 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4539c63-2c89-3140-842f-127b3eb7d8d9 | -4.1495 | -47.991402 | 2026-10-09 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59dabc17-d717-360e-bf40-510059f82ee4 | -10.4671 | -47.8661 | 2026-10-09 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e519a8a1-bb2b-3f3d-94bb-69877375240a | -4.9305 | -45.726299 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b53ab77-b576-351f-9ed8-b8d3da70aaee | -7.8678 | -44.148998 | 2026-10-09 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1a69bab-446c-31fa-b2c2-b9849403deb1 | -13.636 | -44.431099 | 2026-10-09 00:28:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 306b6952-7ca0-3571-8b81-9f91273eab8b | -9.2842 | -47.438702 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7de202e-846e-3185-8934-5ae0c8c7fd50 | -3.8137 | -44.598499 | 2026-10-09 00:28:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aede6ce9-4bb2-3a36-a52d-7bfc02824758 | -9.2924 | -47.428902 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 073cdb7d-b210-354c-9e3d-07e7079ce9b5 | -11.7239 | -43.642502 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| acf9eab9-b0b4-33d9-8c02-a6865c0599db | -5.4195 | -44.626999 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 627e03ef-7fe5-3d1d-a34a-e47f46871e47 | -2.9874 | -54.085602 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7807b4-4aff-3998-a1ef-3d229402ee0c | -6.8274 | -39.559101 | 2026-10-09 00:28:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bf7dd5b6-3350-3530-8106-5e119324c1d9 | -6.2533 | -45.3335 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ae50ccd-a80a-371c-b6a9-975550c29ef1 | -4.2722 | -46.542198 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 029c2832-1b9f-38db-bf2f-c5cac96bc2a2 | -4.7287 | -55.6516 | 2026-10-09 00:28:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6001bc62-bc67-3adb-be01-024157b731aa | -11.613 | -43.698299 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72766590-cc90-3909-b5e0-00682f02d72b | -6.1428 | -47.9268 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f480485a-081b-38ad-a69c-297cf9eb64c1 | -11.8349 | -43.586601 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddba3f2f-0b2b-3628-b1c4-90efd06dccdb | -10.8441 | -47.9482 | 2026-10-09 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f91ee89-3141-3e27-8ee7-b5a127f69475 | 3.5222 | -51.246601 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| abe4297b-dde0-39a6-a268-410bf36b57b8 | -1.5939 | -47.363602 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae94c69a-b280-3be2-96c0-5531051a7baf | -2.8351 | -54.134998 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 320945df-ceab-3235-b712-2105409ada06 | -12.0273 | -43.436501 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06c3ab77-30ca-34a3-8089-4a067090fa6b | -1.5923 | -47.3568 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082df581-235a-3f8b-b378-6f72afe75908 | -5.0883 | -46.1437 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5735239a-77c3-3b98-94a0-3e5a028a043d | -9.4615 | -44.616699 | 2026-10-09 00:28:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09e2129f-be6c-314e-8ff0-a65c505edf4e | -9.4599 | -44.609699 | 2026-10-09 00:28:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa9b26a1-c008-333f-bb04-b75f60ad9adc | -6.372 | -42.522202 | 2026-10-09 00:28:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9a5201ef-e51a-3e31-b974-a08507e1c538 | -11.6309 | -43.597099 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 399f6846-e5ec-397b-a6ac-6fe6a297cb10 | -5.7049 | -53.502499 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa78205-245f-367d-bb39-f7ea162d4c98 | -14.9717 | -47.558998 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dde6a3cf-d5be-329e-b228-3164f8035500 | -11.9963 | -43.4813 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d056a6c-1221-3e85-b3dc-a392540cd187 | -10.7785 | -46.619099 | 2026-10-09 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea6310fb-84f6-3c06-b775-41bdd0583b44 | -14.4296 | -43.928101 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 606de220-9317-304f-8f69-e31a29cfc353 | -5.4171 | -45.868599 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6b843d-6046-372d-a24e-7c8f0fb8885f | -9.8573 | -47.473801 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17514d53-809f-3316-a883-e2b2fcf0c284 | -11.2865 | -41.125099 | 2026-10-09 00:28:00 | METOP-C | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dfcfba5a-5381-391f-ab92-24c44f0cd441 | -18.285299 | -49.520401 | 2026-10-09 00:28:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de1e70db-d83a-3c69-a38d-cf63ef55a6c0 | -8.1888 | -46.361099 | 2026-10-09 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28ca126f-5ca6-38b8-acaa-04cc7169204b | -3.5125 | -54.6549 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c565d8-b563-3399-b2e3-ed9206f05a9c | -15.345 | -42.7836 | 2026-10-09 00:28:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72c6ba37-db34-35bc-bed4-255a510e98ff | -12.0192 | -43.491001 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfe3cc4-d713-35f8-804b-f3e52d866258 | -9.6114 | -40.608101 | 2026-10-09 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4d41aaa5-7a26-38f0-8ad1-15559d060e18 | -11.0043 | -45.417301 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0264b932-1a54-347a-b0be-f7dbf1992308 | -11.9075 | -46.5634 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0455e461-7355-3bea-880e-fe073131eedc | -7.1479 | -46.5868 | 2026-10-09 00:28:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c826df1d-7cae-313f-8e9f-85ed940c45af | -5.0585 | -46.193501 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3568e281-750a-36e2-ad25-a34e296bfb60 | -10.8772 | -49.149399 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e7866d6-af13-38cc-8e84-7da5b50b598f | -5.0941 | -46.214199 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7de7835-d876-3f94-95c4-aaee8db94036 | -8.9947 | -45.915798 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| efe19414-d198-3227-8c5e-98d48748be3d | -11.8431 | -43.577202 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b85c8d48-026b-3c0b-ab56-cc6b2dafab4b | -14.968 | -47.541 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 770b8244-f8cc-3d25-abea-1d74cf3cbc12 | -3.5786 | -54.6768 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87f5c61-fb20-3021-87b0-4dbdc36fc1eb | -3.0889 | -53.7635 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e636d49-867f-3983-9d5d-3c1ef5cd4f64 | -3.0706 | -53.955299 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a5da06-19dc-335b-b1e3-59cbde682e0f | -12.2718 | -48.1521 | 2026-10-09 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18312f40-8a4c-3059-bd91-5b25998dd835 | -6.7237 | -55.124699 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8813cd-1d5a-3754-a254-eaf23c8051c7 | -7.1752 | -52.618301 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9244d05-3773-319a-ab63-6fc182fc9c09 | -13.1597 | -43.2897 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 191f83dd-1ead-39c4-864b-691b899d3ddc | -5.7146 | -53.500401 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e953beac-c1a4-3dfe-b008-3f7e01961050 | -6.851 | -41.756302 | 2026-10-09 00:28:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79995281-bb32-36be-b16b-d2bf38eb31f0 | -6.7334 | -55.1227 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18269dcd-36a9-31bb-89e5-0699eb1d0faa | -4.5305 | -47.040199 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa0f7fb4-3e84-354e-8e80-4572a2477325 | -7.487 | -42.828899 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b0f780e-3110-3eab-b18b-84f54480ecdf | -2.9886 | -53.8629 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db08d3bb-500b-3e33-8050-41ba9e112391 | -5.7555 | -43.8531 | 2026-10-09 00:28:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd73e78-0a48-3398-b46c-7e07f3671219 | -2.7307 | -54.125301 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998a7fc5-abac-3b22-a6fe-406f208488f5 | -7.2554 | -48.070999 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd25c86b-de07-37dc-b90c-e618c4538483 | -3.0955 | -53.792999 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab3f3b0d-1340-3ae5-83f7-846e0160267b | -5.4332 | -43.445702 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README26.md)
