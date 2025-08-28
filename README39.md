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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99aa5a24-9116-327c-9345-a1f8668910b4 | -9.50155 | -46.69854 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c32aab6a-734f-3aad-9823-f430df06766c | -11.56046 | -46.32775 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38321bd8-d4cc-3e45-a7ab-fbbdaf8e8898 | -10.60782 | -49.64777 | 2025-08-28 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f92ba320-b711-3985-96d1-c0c09d2be6b7 | -11.79602 | -46.7881 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fae85c3-6cf1-3919-b61d-4b5cafdb21b2 | -12.81641 | -48.13862 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d1c4ca8-02e6-3801-ac5a-1476936d093a | -10.54069 | -46.70051 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ce1c7fa-3ddb-3822-963d-16d4d620fda1 | -12.95907 | -44.58316 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 207f99b9-cce2-3fb9-a9ff-fd46dba4ff22 | -14.13812 | -45.41384 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a550ba15-dad4-3f67-b97b-fc8ec1eb2970 | -11.55972 | -46.33212 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 67a128c2-2a33-3d84-8679-bf90c41367e3 | -11.91488 | -46.70784 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22c3f674-fe1c-38be-a5b4-27bb96861da7 | -8.43654 | -43.67901 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7ae169a-0fa3-3cd8-bf26-73da0fb1b809 | -11.33461 | -43.53665 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e48eb33d-9866-33c3-b791-fc605e992b34 | -12.87896 | -48.11998 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6208b70c-4982-35e8-aff3-898e6fd7e321 | -9.03427 | -42.70715 | 2025-08-28 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0326d4e-fb95-39ce-a849-e0c7c198476c | -12.50451 | -47.22798 | 2025-08-28 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cdccbed-821e-3b5b-9c34-520853e79f6f | -12.78803 | -48.18198 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f65e3248-67a2-383d-b581-0ea555c0e6d1 | -8.28125 | -45.17797 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4350dda-b8de-363a-960e-a04fd54b056d | -9.45061 | -51.95622 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b7d5645-c988-3302-8197-1df07462ad40 | -13.06795 | -46.33597 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c231b2ac-c9ab-3338-8c9f-8b83ceb7f0de | -8.45085 | -43.65501 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df4bdff6-39f9-3d73-a7a6-9885315483be | -12.79509 | -48.14211 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e33fbc7-43bd-38ad-9ac2-aa8fa7d064d1 | -11.32908 | -43.52845 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 468e560e-db3a-34e4-b4d0-42d5803d297e | -13.52527 | -46.88223 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e3c3a5d2-17d4-34ad-8afd-cb9505b88267 | -11.06554 | -44.59604 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e95cf82e-ff68-36b4-b1f5-59dd11288c26 | -10.53089 | -46.68912 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3c2fd1fa-e800-3920-931e-35bd1eb87095 | -13.53559 | -46.88849 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6b3f7cd-5658-3895-98b7-50ed6313bb6c | -9.45796 | -51.94907 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a5da3ee-b949-3eab-9e46-023dd844ff62 | -11.33737 | -43.54075 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c01a1087-0712-3e76-ba0c-e3a50b3eb5dd | -13.52858 | -46.92883 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25b9042e-81b0-33a2-a8f2-bc095d2590d6 | -13.46029 | -46.84779 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6400017-f1f7-327e-b17f-f7c2f5718800 | -12.69268 | -44.40727 | 2025-08-28 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7adbbc0-bcc9-315a-ab96-d4a9a9cd7ea0 | -8.88318 | -45.72878 | 2025-08-28 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec7c5283-c474-33f6-abf0-32550c14ee22 | -11.57283 | -44.64879 | 2025-08-28 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78f9a268-9507-384c-9e32-a14c466b8467 | -12.71051 | -48.17026 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3b7a283-09e9-31f1-89f0-bcd9928a5344 | -11.5515 | -46.3579 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db72412b-2bc2-3167-8722-37e156f9352f | -8.27764 | -45.17736 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3c440e2-97ef-39e7-bd5d-7378a103aa15 | -8.60347 | -43.99065 | 2025-08-28 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba9a31f-abe3-3a0a-81c0-2aba1aa4cd55 | -13.1756 | -45.29229 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a82e3ef-ed44-3d48-85c1-4670b2339fdd | -13.59238 | -48.14871 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aa7e724-e7e9-33f0-b024-dcb314cf2514 | -12.81245 | -48.13764 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f983f96-a4b5-325c-bb45-713277a1acc2 | -8.28608 | -45.14893 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2a13daf6-06d3-3de5-b08e-685cb5bebbea | -14.5045 | -43.85289 | 2025-08-28 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c2abbc1-fcb9-32ef-947d-73148b21fb9f | -11.56391 | -46.39618 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eb1f60a-ac36-3eed-9d10-c28572c28670 | -8.29399 | -45.14592 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| df5163fc-9e8b-35ee-bee6-9bb55b66bac1 | -12.68435 | -48.17725 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e57bd55f-d586-3e27-a6a1-b715bb3136f3 | -13.08165 | -46.34277 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 141c2201-fdaa-3bf8-aca4-9ce9785c6d16 | -13.73742 | -42.68552 | 2025-08-28 04:08:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9f12985-336c-34bd-b9e2-44f0c25c87b5 | -13.50073 | -46.85558 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa1fa312-2a2c-36f9-a241-c95687502726 | -12.86773 | -48.11347 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fad7355f-8636-37c3-ad87-7f044c8d0081 | -12.94788 | -46.33062 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c568861a-6dec-317d-8aef-84b22e2990df | -9.65856 | -48.30729 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd244a59-3085-37fc-9e5e-0bf1aff17d5f | -8.47295 | -43.64733 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34cc40af-1973-3062-8f17-bbbc9afd566d | -14.23441 | -48.02529 | 2025-08-28 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 697c70be-0f1f-3b03-81a2-e97aa771f1dd | -11.32575 | -43.5279 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d61ca40e-eb6f-3f89-8bb3-4503d35a2a98 | -11.57344 | -46.3848 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdc4a475-97d3-3359-be7d-2e1569e1f81f | -11.55377 | -46.34467 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 413a7886-a9f2-3666-b857-518b45ab4af3 | -11.5471 | -46.36146 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa54a9ee-7403-30ff-94b5-67714ea9e3f9 | -11.65495 | -44.87606 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07277551-3228-3280-afa8-3e5c35495e7c | -9.45181 | -51.94965 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 472adbf2-f6ef-35f3-8ac5-c26abb24a56f | -11.56466 | -46.39177 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb44b601-1f75-3d49-87f1-a5caae84584f | -13.60136 | -48.22502 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f5bf573-32f7-35d5-8d06-35989eddcb1c | -7.89814 | -44.77738 | 2025-08-28 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df9aa815-950e-38e6-a9da-8e9d36aab698 | -8.27404 | -45.17674 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cd00d54-31eb-3d72-8099-21aaa51264fe | -8.2883 | -45.15785 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4aa3bf12-544e-3208-97eb-2c92e464180f | -11.31349 | -43.54045 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 939abbee-5a98-3d48-af12-e0cd60fa5492 | -7.76334 | -44.06903 | 2025-08-28 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5a231b9-b879-3eaf-9934-119f2719777c | -8.25205 | -47.22669 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 472f773d-d514-3f38-98b9-230b1d590de0 | -9.66848 | -48.31681 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1edd817-3185-33a5-b79c-40b2e6f5396b | -9.65107 | -40.59573 | 2025-08-28 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7a701258-5f6f-339c-a1ee-bbbcd3c53fd8 | -8.2847 | -45.15725 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 14d1a051-7439-3fc1-a282-b55108c3aa45 | -12.72052 | -48.18436 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af27055-fc71-3428-aeae-82ecbbacf66e | -7.94647 | -42.62561 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0088697-d293-3e20-a653-75b9b268e336 | -10.53063 | -46.71345 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85a2dcb1-0e08-310c-b85f-12c1a57619cc | -10.32983 | -46.77728 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e6912d6e-969f-33ec-8660-fa512d434d1f | -12.95751 | -44.57152 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a89a3021-aea8-3323-a23e-516cdc8b0e08 | -12.43568 | -45.96566 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b8b39bf-962c-3b53-ab03-5123c677ee16 | -11.60984 | -46.21506 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5436cdb3-7e96-3289-8aa9-73244a14ee53 | -13.18721 | -45.28637 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85665aca-56f3-3fec-af98-1c0ab891ef68 | -11.24069 | -45.00078 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e21b6ce1-cd74-3d5f-ad7f-01c6c4e0dec0 | -8.28239 | -47.22071 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0e1410af-eef5-34db-853e-0784365b5d5a | -13.61067 | -48.19626 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 656f6f87-2323-3fb7-ac5c-a0614ffc1f3e | -8.85998 | -47.18741 | 2025-08-28 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07c768d3-d273-382d-8795-6d509da2765f | -14.12847 | -45.4082 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96111100-8ae2-37d7-bd1d-8e65b27d4a11 | -12.6937 | -48.17134 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 332def7c-9484-34e8-906d-9a6a860c2210 | -11.23103 | -55.05777 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7783d5ea-9b2a-3e43-b22a-85279e64b116 | -12.88744 | -48.09568 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 411271d0-403d-3c23-8a2f-2633587fba11 | -12.80732 | -48.16674 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b34f8ea6-c488-34d5-a540-35c64c877a7a | -13.08174 | -46.32059 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ddbd26a-ed3c-3a5b-9967-2f888b7c43d4 | -8.4417 | -43.66859 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d7dcb4-4490-3961-aa1a-74221306063f | -12.7874 | -48.18553 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb0e6570-da14-3c8b-a0b9-fc30c74e527c | -12.80652 | -48.14777 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ce2d20a-726c-35a7-aa66-03ba07bec1d2 | -7.25793 | -45.35635 | 2025-08-28 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3068697-e827-38db-ac72-56b25520a849 | -9.65786 | -48.31137 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03bd02d9-239b-329f-8603-cf362deb34c4 | -9.19469 | -43.25726 | 2025-08-28 04:08:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d258f97-6c79-3d13-828b-a966e574c590 | -10.6987 | -47.09319 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62b3f262-590d-39d6-85cd-2f69fdd9a115 | -12.43498 | -45.96983 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07cad52b-1f63-31cc-aa04-5c0a6abb47c4 | -11.84029 | -46.80075 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc78ad39-f47f-31a2-8521-91e16d460b73 | -12.68902 | -48.17434 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cac3c738-9c7d-3e6e-b09a-36f055e7f177 | -14.14003 | -45.40235 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8040b096-07db-3e47-a1a3-8a138f328075 | -11.21718 | -55.06023 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README40.md)
