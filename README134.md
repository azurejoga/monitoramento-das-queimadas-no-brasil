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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf574b27-138b-3988-9007-167f66dcc076 | -9.07793 | -65.48355 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d358579-c756-3330-88e4-ac164f28788e | -2.89194 | -54.16389 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbb9225d-3a0e-3bb1-9f39-4af455b02d0d | -3.26141 | -54.65937 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b32c1e2-2e64-3c46-978f-0798935fcab1 | -3.15165 | -54.0922 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd0582b0-1b08-3efe-a4d1-f80031ac70ef | -6.51192 | -55.40263 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 364b8b7d-6450-3a10-90c6-14b0f95b487f | -3.08721 | -54.29885 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a29e412-c3a3-34cf-a019-61cb73a0cca1 | -3.59396 | -58.26699 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4440e2b9-c57b-3dfb-8619-b5f5820fd673 | -2.99354 | -54.04502 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4349a254-79fe-3d1c-8b53-8502eaea1327 | -3.02522 | -53.90969 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f4eb98-6d9b-3f66-a522-9c0a05906257 | -3.47876 | -50.08677 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c36546d3-d606-31d0-9dbb-e5fa007add7a | -3.78753 | -50.75938 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bd9fc95-3f5a-3192-8032-bfa4b75ca097 | -2.7167 | -57.46488 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dad31454-0d2c-38d0-bca1-d3206c50d14c | -2.49353 | -58.07299 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aa6440c-2012-3823-879e-60dc6179e4d0 | -3.12978 | -53.70571 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5033dabf-3840-3fdd-ad01-095cd6e39ac5 | -7.18595 | -52.62223 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed6fa4dc-810a-3f48-9715-d66ca3ed85b9 | -2.72285 | -57.46947 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 196a8e1b-5c9a-3f24-8649-797d983a3bb0 | -4.80854 | -54.67438 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf80478-55ad-39a8-8876-bdbd148a3530 | -1.45501 | -54.7835 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a7fbe55-58ca-3b35-afdf-30404eb33599 | -1.53069 | -54.54767 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64d1868e-6f9f-3917-af7d-d210a3d10511 | -2.38607 | -56.13849 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4be9e8f-13e6-3802-9758-df57163c3f82 | -5.73979 | -45.16284 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0195b0e-7c24-3708-8ac8-a64b0a825ade | -3.05704 | -53.91464 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed7b7278-cdb4-332e-8ab7-94352a68f4ff | -3.23632 | -50.17551 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af14c865-a5ed-34df-ab7c-db273ace0930 | -2.89416 | -56.67163 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9b03689-81b8-3cef-8d3f-5ee58bb2a4ab | -4.8987 | -54.99368 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db1cda50-10e0-36c0-94b0-bda2177be80b | -3.00639 | -54.055 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| be858854-5283-3485-8af0-3900af9b369b | -1.43052 | -53.23271 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d624fa-ad16-3312-8133-2bd6ae742309 | -3.14982 | -54.1039 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f863fc32-bdd9-3850-9d91-49e90664aa89 | -2.05003 | -56.38266 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4462095e-e45b-3584-a271-e270e41a352c | -2.88607 | -54.17867 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2edd994-ba69-33fb-83c6-d4b0cde5d32e | -2.37277 | -56.1364 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba879e1-ce2c-3a26-a96a-a6c6e51dee8f | -9.47582 | -64.35217 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24f11d0e-d73f-37d0-a451-e6c77bd729e1 | -3.52843 | -54.67345 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 51941764-9d1f-3003-8667-ddedc03b520d | -2.93571 | -48.86447 | 2026-10-08 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92c4254c-b5a7-3cf0-b93f-dbafa151f5d2 | -3.35666 | -58.20026 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7d66731-f565-3da6-a79e-2769954afcee | -3.64927 | -55.50539 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c889935-250a-321b-846c-f351bb4cd108 | -3.22729 | -53.88709 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85312369-2a59-3fca-965f-7a62622b5da8 | -3.30332 | -54.02295 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 06c9de3f-f151-3fde-b066-63254bdc6203 | -4.10758 | -54.62117 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dfdd83c-5d27-3329-a076-741fafb63cf7 | -2.41173 | -56.53175 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4759231a-325f-3a5a-8889-813b6e56994a | -3.01844 | -57.73759 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f908d68-fc2b-35c1-8b5b-50c70e9f6ff3 | -3.00971 | -54.10312 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1fd0c6a5-6054-35d3-b8e1-e7a88e3c625a | -3.5158 | -59.32034 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b264e4-017e-3990-9ea7-135e7d549596 | -2.94326 | -54.15613 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 174918d0-48db-3a10-9535-69b4cca63993 | -4.74606 | -55.65356 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 638452d6-aa62-37fc-9039-b4834f01c4cd | -3.172 | -50.44794 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f23c080-d090-387f-a448-627b4a84262d | -2.98332 | -54.13457 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b87942b2-3fe5-37b5-96a1-3b21d74e64a5 | -4.93785 | -55.81027 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 301c2d17-21cc-354e-8621-0ac06b7ce61c | -3.04878 | -51.22436 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e31cc8c-b17b-3d10-8c77-b90046d110b5 | -3.82322 | -58.99973 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7c1c36-504f-3612-8119-ef7eac5a6069 | -3.59957 | -57.68359 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b394956-3d4c-3a77-96dd-840e3f6f09bb | -5.23517 | -56.1137 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e187710d-09ac-36ab-af21-5fae03cbca22 | -3.05289 | -54.21631 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac02c7bf-7b0f-31af-b881-c6832ef63177 | -7.86281 | -45.40043 | 2026-10-08 05:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f744bf5a-902f-390b-bda3-08a9b04d7e4a | -4.98943 | -56.14725 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ef5575-9ea1-3f52-a35e-454ccf082a0d | -2.88933 | -59.2015 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23df2364-46e7-35b2-9e35-fa1cbe9f0a7d | -3.07631 | -54.25415 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662a5d1c-9e2a-37db-8a82-9f2ffec3ad4f | -2.71002 | -56.52576 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46a9d6fe-318c-37e8-9e0b-00006cebd3db | -3.01732 | -54.10035 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0174efe9-285a-36a3-8308-c79232b1e23f | -1.83806 | -59.95744 | 2026-10-08 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31173c68-c007-3422-b7a8-03b864a419ff | -6.63061 | -43.72494 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0dc363db-7f54-3987-8ade-5164ebc65dd5 | -3.59903 | -54.57642 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6669d157-bb67-3b88-930c-bbcaacafe41b | -3.58515 | -54.31421 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb3ff6d1-dae6-3d83-8e85-7d9a611c1dcc | -4.51897 | -54.89452 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f58fe3ab-8362-3acd-a444-6c50812f1d9b | -2.88869 | -59.20547 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6eb715c1-683d-3f9f-8249-9ead0edf190c | -3.00652 | -54.74942 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9445275-2324-3e5f-9489-7d61b9e53785 | -3.26804 | -54.01758 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85b740f7-55cb-3af4-b1ee-19b5f0aebf35 | -4.08707 | -55.33488 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e619ea7-6853-3a58-abba-6fa94804a4a5 | -3.29866 | -54.66892 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b383a310-2a69-3ccd-ab31-aad092fe649b | -2.56744 | -56.16674 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbef6990-4fda-31b0-b65b-548488805051 | -4.26621 | -54.87943 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8447b864-a9b4-336d-be17-f1ed115fd0e7 | -3.13739 | -54.36494 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d03cb0d4-2cf7-3d2d-b9b9-979cfcff1195 | -2.76874 | -54.09546 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf1dce5b-8eff-3741-a6f6-ac45c8d54716 | -3.2051 | -50.55017 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 159fd193-3d97-3c9e-9251-7553806906a4 | -3.11716 | -53.78584 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bea4df87-bf69-3ba7-bb9e-a052ef03fb45 | -2.46574 | -56.08366 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07e21ffb-cc99-3217-8ac8-bd10397931bb | -3.58166 | -54.31367 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50a99333-a1db-34e5-a4cb-f3b1df3edabc | -3.0222 | -54.18403 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a49c8b50-8710-3208-9933-a9682f5c1dc6 | -2.93096 | -54.16604 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0de7e3-6509-36ea-b206-e20022daeff9 | -3.70961 | -59.64353 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 293b4452-b076-3680-8e8e-8972d4425fff | -9.68636 | -65.01788 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77254c3b-e83f-3668-9322-09e16e31ca7f | -3.10899 | -53.76822 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d555e83-f7ef-36ae-9a02-2ee9995f8056 | -2.57022 | -56.17072 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df8b37d6-ba7f-3834-b947-ffd672f46a4d | -3.27498 | -51.06979 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6825a1d0-ccfe-3ca9-bacc-c3a8f8ad6120 | -3.32905 | -58.15485 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e770b293-f2eb-3264-bce3-46fc6bb4d9e1 | -3.01432 | -54.11968 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8d18005e-f6f1-3ca1-80b6-3f3486edf3f9 | -6.6826 | -55.08828 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2dfacfb1-adee-317f-a3e1-09da7f1fb72f | -2.72062 | -57.46188 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8f094ec-f84b-3c40-be35-ac83383d7639 | -2.94037 | -54.15175 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f520f292-6e00-324e-acff-35f2037d89d3 | -3.65225 | -54.28058 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f510aeb9-00ae-3ec9-b410-1e2297443b16 | -3.00267 | -57.74971 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 428527ec-9582-33ff-83b5-9a69413a621f | -7.22923 | -55.16508 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed1f1868-26ce-30ce-bd44-5063b377149e | -2.82789 | -54.13529 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2edafe2a-4d54-3e7b-9a79-8db1610dd3ab | -3.0043 | -57.16918 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b10b435-a720-3d82-953b-07eceab46083 | -3.45242 | -58.06274 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4cac787-1038-33a1-82e4-a6aaf5690bcd | -4.79541 | -55.71903 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54a419e3-01b1-3820-95c2-d3dc94cbeb89 | -3.0844 | -54.27104 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 692acd7c-a16a-39f6-a387-fab76eba2044 | -3.71815 | -54.22638 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 372d66c4-3792-36d1-8512-4aa47221c33c | -4.26849 | -54.86462 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79aa3faf-5618-3e32-abcd-a615d6bfa860 | -2.48853 | -56.11204 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README135.md)
