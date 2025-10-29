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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a99657-0664-3a2b-ad43-1ef37c1dc240 | -13.66941 | -47.19441 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3f4aba8-dc73-30a7-96c2-1519d493db56 | -12.43683 | -43.75204 | 2025-10-29 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c107fa32-7ec5-3127-9814-144e80620ee9 | -13.21916 | -47.55468 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14237675-0fd8-3a48-b0db-e76c3506b792 | -13.31711 | -42.42294 | 2025-10-29 04:25:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b6c704af-5508-3bc2-9587-59c349d26679 | -15.743 | -45.10546 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f501b6a-e75e-357f-9823-a47f4663fe3e | -13.22932 | -47.0659 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 785ea54e-49b2-39f2-bae0-adf987becd32 | -13.57699 | -49.59592 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6b73418-6fe3-3c47-8fd2-9de8587776d0 | -12.75002 | -45.1669 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3646ec14-fe0a-30d8-949d-5df6e3145094 | -13.60764 | -46.48141 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f5e7c1-4345-333c-8d3f-83ae7d284580 | -14.59736 | -48.4034 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bf60c98-1c39-3be8-a5ca-a0c8ac0d6095 | -13.37957 | -47.41206 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 484c2a31-0507-329c-aebd-466ccb04fe2f | -13.64258 | -47.02067 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 343f9e46-3b0c-3ecc-80f2-555a641b5fa0 | -13.55651 | -48.05917 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 732f5845-f36d-3ead-8632-1bbe22b0929d | -11.03554 | -47.84597 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2133ceb-27d1-331b-9a56-56d2d4e9d74b | -13.56262 | -49.57116 | 2025-10-29 04:25:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 239e4230-64f1-340f-802e-a42efcea1de2 | -11.79016 | -44.1661 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fca59c2-8eca-36c6-b247-a10737c812e3 | -13.56837 | -47.33966 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1447832e-4684-3683-a937-403bf9075aa4 | -12.05092 | -47.8191 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3ea0c93-b6dc-352f-a986-93fc0a24a591 | -12.9758 | -47.91087 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00ddbdc9-ce6c-33dc-b535-7047d501c59d | -11.33769 | -46.0705 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dca98388-1d2d-371a-8f57-6db29dba4422 | -13.64415 | -48.43468 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de856c02-dd57-3e8d-9661-6d048fe5a842 | -11.26047 | -47.81749 | 2025-10-29 04:25:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 074d032d-2ff5-3a84-8036-497ade350517 | -13.04124 | -47.57671 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f85435b2-9f6a-3286-957d-c9893a881547 | -13.2329 | -47.72928 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e16197e-f55f-3e38-a4fb-51fa84d5549b | -13.63264 | -46.51079 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58f65de4-f52f-380f-a8c5-2a07febd13b4 | -13.93971 | -50.33948 | 2025-10-29 04:25:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f181f8e8-7fc5-3e71-99a4-021393acf15c | -10.85605 | -50.14743 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15cc8ccd-4eb3-3e83-9455-7de70451768d | -14.3251 | -46.51942 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 088675fc-72bc-33f9-b20e-203bf7032a8f | -13.63715 | -46.4824 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 688de30a-ac12-3a22-9b67-d3d473acc0ca | -14.27208 | -47.31654 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99d9f536-b7ca-3218-a1bb-aa99b2db2a91 | -12.91211 | -45.04041 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f8e524-1b9f-379f-b6d1-73baa102af80 | -14.97813 | -48.19417 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba9f3b1-8105-3bd8-80da-da955b771a5c | -13.94576 | -48.47806 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac9b76ab-dd50-3e1a-a2c5-42867b853944 | -11.93346 | -51.33422 | 2025-10-29 04:25:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a902ce-81fd-3905-9292-477dcf9700ce | -13.54293 | -47.13552 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2704c1ad-8f4a-37f5-8d55-8a6ce960543b | -15.31985 | -47.85431 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac9fac3-eaec-3934-a74c-c45ae9bacfeb | -13.53913 | -43.35128 | 2025-10-29 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5017bd0b-1568-3956-8356-a0e96d5179d3 | -12.12739 | -46.7222 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed6bae25-d47f-39bf-b1e3-a094e97ac398 | -14.66422 | -48.39896 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8018a26f-e652-3e55-ae2b-f42004f42d7d | -13.70229 | -47.67955 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158bbced-6fdb-3306-b49e-cbc9623d9c7f | -13.63912 | -47.0421 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d37112f-452f-3ca9-ac76-29a28f4f242a | -13.63428 | -46.52198 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 253ad7d4-8dcd-34c8-9695-959b299d35c1 | -12.46483 | -43.58644 | 2025-10-29 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dc4635d-df0d-383a-b046-07e396f77424 | -12.35811 | -50.15517 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f05295d8-33f8-3526-bc32-f688dda97373 | -15.19399 | -47.20598 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12ee6a34-f502-336c-aa44-ec2ea4e61770 | -13.94363 | -48.48136 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dae88f2-977a-3b3f-9811-14366fd44cb7 | -13.17844 | -48.4441 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188a17d1-7fad-3297-9419-822690ec52cf | -15.792 | -45.19414 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff1d75f8-e6ec-3c73-ba6e-8fe42f000472 | -12.95166 | -42.47796 | 2025-10-29 04:25:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6deb8c3-1d85-3aba-8ca0-997ddd78b799 | -13.64318 | -46.50889 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39b23962-d2ea-3459-95c5-f88a2360ae01 | -14.98935 | -47.86573 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad925945-202f-3110-8042-fb831e32ca79 | -13.63208 | -46.51434 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 257a05ec-c955-30ac-b404-75c38a95be66 | -14.30899 | -46.53503 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2940b2f-fce6-35fd-8361-cc068485dc8b | -13.74058 | -48.39925 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe61cf7e-1a75-3634-acc2-6720c54daa91 | -13.94771 | -48.47816 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 223f3d0c-80aa-3c2c-b4a0-bec4369ffb55 | -13.64419 | -47.03191 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b2081e2-c7e7-34f2-98b2-3bb6b44355f0 | -12.48373 | -44.2088 | 2025-10-29 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af2ede26-869f-3c2f-8031-8be08e8a8757 | -13.54627 | -47.13608 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2095a3f-98c0-3b44-ab40-496d7ce6e696 | -12.80789 | -47.26945 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a44d55c9-73bc-308f-8130-ab416399e127 | -12.06709 | -45.71579 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| adf1b456-af13-3a07-bb3f-1df0bc99bb98 | -12.53661 | -47.54215 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d692fb6d-e313-34fb-a8f6-632dc5ff2302 | -17.53866 | -44.61399 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4223c79-0c28-3988-842f-fb06eac6b068 | -13.66564 | -47.17522 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de295d36-656c-3ba9-a2f5-ba6c34a0888d | -13.42017 | -47.37433 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 559500bb-70aa-3122-995d-cb7be7bc2bb8 | -11.25766 | -47.81312 | 2025-10-29 04:25:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 098efea7-0a56-38de-97c4-0ed55e222af9 | -13.66007 | -48.4454 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f30f9592-528b-30a3-93b2-1121c00b141e | -13.64694 | -47.03609 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e54c28e7-978c-3656-8199-49879a80f063 | -11.04175 | -47.8512 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d53d6694-52b8-3326-9012-f3194e40fa60 | -11.78332 | -44.16502 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89a9b3e8-5aca-357d-a8eb-995b7cdb1824 | -13.05201 | -48.62347 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75f6a0d0-311d-39fa-87b4-2c15eea3051e | -18.36716 | -46.41908 | 2025-10-29 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 001f164e-aa2e-3fa3-b31b-8d3e3e93f898 | -13.5747 | -49.60921 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f74efaf2-27b7-3bd1-8cfc-0195662093a3 | -13.69676 | -47.67098 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9457712-fcd4-3bfa-bb62-f301838a55e3 | -13.89475 | -48.50803 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac2a45b7-c455-3763-8c3c-53ba7504a456 | -12.3016 | -47.26383 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68329119-db6f-306a-a2cc-982223ac4c89 | -12.00781 | -46.77224 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00ac6204-4527-304e-86f6-85933ed3d71e | -12.24944 | -47.9296 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d1d0f55-ec92-39e1-a444-3339a40b6d5e | -15.21671 | -47.21349 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b689ef-0e2f-375d-a40e-8cb201f6b980 | -18.93036 | -45.02858 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d6d285f-1075-3587-a9fc-1021ce92a6dd | -19.3403 | -43.05796 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d9c282c7-4452-304e-b09a-135161137a82 | -13.64361 | -47.0355 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a66d533-e175-3d5e-a4c4-2223a16b4c59 | -12.0913 | -47.25443 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 007fecf5-68ff-3c2e-9f3b-519df04c34c0 | -14.73491 | -48.16074 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1affa235-eb52-337d-9a41-2ad0dc70919b | -15.09851 | -43.8354 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 511d89a2-f03a-37de-a807-edb837c09637 | -13.6806 | -47.18889 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4184ec14-fa20-3e0b-9e45-d05169f59b0d | -12.15279 | -47.68679 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f8755d6-c4b3-3ff2-9dbf-5724c1c37cc1 | -12.37181 | -50.1597 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f63d11b-e4c6-361a-bb1f-b7c93e9dd6b7 | -12.19147 | -46.72175 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61f62966-6c40-398b-8d5d-8d08b4ac10af | -14.52304 | -48.00337 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 56ce2f5e-bd92-3758-9710-396764cd92f8 | -11.06307 | -47.53455 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c909196-56fa-3c15-a520-e20cf5a52767 | -19.37033 | -43.64235 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6567ace7-c88e-3921-8973-b6e98480d533 | -12.52401 | -44.88655 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96b4a259-593d-3ab5-9eba-f0748c298f5d | -13.92864 | -48.43164 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17c2c589-88d7-3da5-834e-38fe5dc085c1 | -14.49403 | -47.88406 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7ba59ae-36ef-3f3e-b4c2-665c07c0034c | -14.07384 | -41.74432 | 2025-10-29 04:25:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 14517aad-1fdb-3df1-9981-99b98d9fe60a | -17.48624 | -44.07167 | 2025-10-29 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5ae7f7d-12c4-3f0c-a810-b9e366839656 | -11.99664 | -46.77771 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0b0363fb-e92b-35e9-a54a-1ade76ced95c | -13.6372 | -46.46055 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38c58f88-ccbc-320d-8a26-530ee292ab4b | -12.52984 | -47.54101 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 324df3a4-ed4c-37bc-8dff-316dd7f6ca04 | -17.56881 | -44.75063 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README50.md)
