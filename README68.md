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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb9e43cc-85fd-3a22-8d0e-e2a81e5a9da7 | -10.9217 | -46.72264 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 493e8960-85f3-3520-a17a-695d44444f6f | -9.0822 | -46.76503 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0cf0957-e083-30f4-a995-948f87a74ada | -12.20829 | -47.78823 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ef19a88-16f7-371e-a9c8-f9356cdafdea | -11.79951 | -47.93185 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe349930-3fb3-363e-ad7d-750cf2730807 | -14.31219 | -45.87324 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea901751-b4ce-3500-afc0-215c6d99b89b | -11.13343 | -43.39758 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33e07aab-b048-3c26-b84e-809726f3907b | -13.49216 | -48.57922 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0d681ea-045c-32b5-931a-58a07e6e41c5 | -9.71075 | -48.95199 | 2025-10-03 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a16a761-e1c5-340b-bba7-0fc5e2960c31 | -13.76678 | -47.53591 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0005b357-c7d1-3c19-b688-c00e841db786 | -12.8716 | -47.03568 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc607b33-eac3-319c-82c4-e66b90b9a47b | -11.06889 | -47.80256 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a87578b-a4ec-39a6-97ca-0403ca41d528 | -13.77589 | -47.57393 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8db9706-eef5-3e91-b6f3-2acde5fad322 | -11.48986 | -43.49964 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 584e4dd3-aa9e-3b84-b20b-7ec4823caecf | -12.80204 | -47.03497 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a56af228-df66-3087-b044-f74858f55adc | -14.21041 | -46.08776 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d49dd569-a3b8-345f-bedf-addccde0fdd7 | -13.26544 | -47.26159 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddf8fd6d-d29a-3e85-9f5b-cd6abf3c837c | -11.16784 | -47.18287 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4af5f81-afc8-3b87-8a91-ded5101fbea5 | -9.94168 | -43.74588 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a8c2012-9a45-38ee-8cb5-a412f3ad63ec | -13.80594 | -48.06174 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 999871b6-580a-30ac-81de-c9dbc9846fbd | -9.94447 | -43.75007 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fff83b0c-c2ca-397d-b817-cbec6aa11f59 | -13.86843 | -47.93819 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cdf8882a-df20-3cce-b7e1-29e754ebd3e7 | -10.91757 | -47.05308 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21ad30e6-b6fd-3fb9-81f5-b6617654c810 | -12.68491 | -48.58329 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31cc0827-7346-3f9b-b4d8-a556c5a4aa4e | -13.68397 | -48.64663 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a7bc3b3-a463-3276-bcb6-70b6882338cd | -11.10756 | -47.83936 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 330f5847-d3ee-3436-96b9-02adc0b03420 | -9.95439 | -43.71061 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c73ead78-f1a4-3ec3-8276-45081823d0ac | -10.00346 | -50.24518 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d64a1cb5-ef3c-3b95-8601-688e46e6ec62 | -12.62221 | -47.00193 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 390485a3-0905-396b-9a0c-15698dcb05ba | -13.1231 | -47.86308 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b74e2e9-9314-3b02-8dda-bd73646739fd | -12.8401 | -46.8595 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d1cc91d-cc74-3d6d-a220-a45e6fdf9a8b | -13.19175 | -47.7898 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 333d370e-b6cf-39be-a117-5456d5444705 | -13.26347 | -47.25053 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b4ef0bc-adbc-3962-8cb6-dc1feaae92f5 | -11.65511 | -46.98277 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f8fe01a-291f-3674-8d62-93e2a19b9419 | -10.7528 | -45.34798 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb631c7c-d9b7-36bc-a983-632ff3fc1664 | -12.29578 | -45.36317 | 2025-10-03 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f57f2cf-c85e-3d61-b997-9332d4434f4f | -10.30458 | -48.28866 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf0dd09f-4b46-3914-aa2a-18125561849b | -11.91378 | -46.26626 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfdda28d-aa38-348d-83ce-e2f686d59180 | -9.38273 | -45.8543 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efbeb99c-e1b9-3da9-b1ec-51623515b3ac | -13.38904 | -48.13071 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e170e1fe-aa14-3fd9-aa47-b411cef7aac9 | -10.93314 | -46.72463 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8252393a-83de-396a-8736-62cd387e03aa | -9.95498 | -43.70697 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 075ce6cc-da0d-3d17-b2d1-e0827f38802b | -10.76045 | -45.3396 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2e0ba5e-b49f-3877-82cc-a8e8cb36051b | -9.92034 | -43.7647 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfbd0949-3690-39d2-9d62-4fbe097fbd6c | -10.07096 | -48.18777 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adec43fd-59b5-3b76-86bd-61752a357a13 | -9.95305 | -43.66927 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba115fc8-ce3c-3538-86b6-1a884dbcebca | -13.52918 | -47.28467 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aafd55d-cc59-3273-a9cc-a9499c3701f6 | -13.16744 | -47.38038 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1680da0-2601-3ef8-8af5-2489057353ba | -12.12054 | -43.44562 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a5158a2-fe3e-33ce-b48a-5e61dd5d68a6 | -11.46604 | -44.96272 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2ee3355-cc83-38bd-9fe4-07e6c24b6902 | -11.67882 | -47.49834 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3d45f4b-0347-3cf6-8181-531442d9be08 | -14.37938 | -45.94678 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96876c28-9e8b-3d44-853e-ea2c0101cddc | -13.76713 | -48.05999 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff811df3-3598-3268-9bfc-ac91848545be | -10.91846 | -46.74161 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 889aa175-2247-377d-a133-05861bdd5eb5 | -13.82731 | -43.23778 | 2025-10-03 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5d2cb83c-eb8c-3fed-9155-34322f47bf69 | -11.4958 | -45.00652 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e41a5de-6186-3264-a2e5-d90792321602 | -12.3878 | -46.51662 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37143363-ceb9-3981-8265-fc3a5b445782 | -12.7905 | -46.87848 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a46c298-c545-380f-8abf-8d52e5fc5ea9 | -13.96799 | -48.16121 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c95ce37-8670-3b3e-a651-47faee565a9a | -11.30753 | -47.83864 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f9a61e0-d6b8-3af0-8c8e-db54d0bf167f | -11.35505 | -44.93679 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 138c7a7e-5626-382b-81db-dded3bb7b207 | -14.35606 | -43.85566 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e9f7321-1c92-33ac-a119-fe0cbb9139e1 | -13.76138 | -48.06955 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9068a5bd-c349-3262-9751-4de96b22418a | -11.80447 | -45.01755 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcc84c81-612f-3dd0-9252-ad5cb10bd01d | -13.57118 | -47.26778 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65e8224e-f0fb-3c64-a024-8548525d9e65 | -12.944 | -48.44859 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c15f645-7de2-3c70-95f3-09c189a8bd98 | -9.75991 | -47.81487 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c895c8cf-673e-3a77-9179-73c13f0ad772 | -13.67803 | -48.03272 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68608fd7-f642-362c-a4cd-f44bb005567c | -12.11367 | -44.20501 | 2025-10-03 04:12:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8a8d9f8-00a8-3481-9c6f-0d94089824fe | -14.30121 | -46.02472 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 430c3ae0-4d77-3a2b-bb89-9837f2765ab0 | -8.60915 | -54.96951 | 2025-10-03 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3b30f5f-b443-30b7-8185-0751dd9055f9 | -12.61662 | -46.96635 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2d41b1b-5785-3213-a795-4b904e3a7324 | -14.3019 | -46.02065 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c933810d-fd8b-3852-bf4e-fa3ae194c8b2 | -13.71217 | -43.89533 | 2025-10-03 04:12:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b2a894-e789-30d2-9a70-790bf69f5356 | -13.30685 | -47.81954 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ef7281-519f-384d-8a91-1ebc935bdef8 | -11.34712 | -44.9633 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 446438bc-6462-30df-bcc3-8e90d360d826 | -10.00533 | -50.24645 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| a82a22b4-8cea-3e4c-8141-5826622758c0 | -13.20944 | -47.82724 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a87b5ce2-1fe5-342b-89c4-ec21edeb869c | -13.76588 | -47.54098 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93c7ae87-96d0-3bf4-ab60-1f1fe403e90c | -9.76967 | -46.21775 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38b79d25-f8c5-303c-9741-6f2c4ec01fbd | -10.0054 | -50.2624 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33b61ff4-256a-3c12-b80b-bf891ee57606 | -11.06607 | -47.79472 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1ec976c-073e-3516-bd37-8a712bb80a49 | -9.94733 | -43.57557 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 389956da-5c27-39b5-a3cc-7ca054ac0af6 | -15.103 | -43.46898 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c5e85597-3030-3327-a70c-dd7e4bd47276 | -9.91563 | -43.79391 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc16fd68-941c-3a36-92b6-4523113f2519 | -13.52291 | -47.2533 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 882904d6-9f14-3599-8115-fdf9d178d18c | -15.08084 | -42.12014 | 2025-10-03 04:12:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| caa45aae-9815-38ae-b26b-021de29d3881 | -11.83821 | -44.94354 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33195d6b-df13-3bb0-bb1c-a6f32d59dde0 | -12.9268 | -45.08395 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd055db-e32f-340f-a67d-77646f777bae | -13.35056 | -47.33681 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffdf7ce2-24ca-312b-a764-255ac49ccc12 | -9.91548 | -43.73018 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4dd3c208-5a52-3460-a6fe-2c8dcdd833fd | -13.84972 | -47.92956 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6750edff-2b44-3b46-a1cf-6119787e4386 | -12.6074 | -46.97472 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2b4f08ea-cc33-326d-8ce9-42f4ef6e190e | -11.18226 | -47.74755 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1471e349-6683-36c7-931b-f32dd3a99642 | -11.62245 | -45.06737 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43e4328b-2489-3806-b72c-d1ff9d41e0cb | -11.80643 | -45.00582 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c827c48b-e0c2-3acc-be04-b18db673fb66 | -10.9657 | -44.3239 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91457a52-43c3-3457-8ef8-71a36e218d9d | -13.96807 | -48.1259 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15a47fe6-3ad5-3bc0-8792-3e088423b50a | -12.6041 | -46.99391 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a419f909-f8a4-350d-8fb8-a49c710b5de7 | -13.23003 | -46.43911 | 2025-10-03 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36690634-5bbf-338d-a792-ab332ad2041a | -11.14488 | -47.19925 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
