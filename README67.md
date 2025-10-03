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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f53bed-e398-3822-94f0-5d69c4b0805e | -8.87836 | -50.90136 | 2025-10-03 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b68ad22-516e-3dba-ad3d-3ccaa601c00c | -9.43042 | -45.46325 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec52a09-5556-3925-aef6-80d62918954e | -9.9093 | -43.72543 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 6287dd33-adee-3529-be57-f8247246ec1a | -11.46443 | -45.03804 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32821a36-7b58-3a4c-8de2-88111cea352b | -13.27596 | -47.26865 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a11a0690-075c-38cf-8581-67dc903bfcda | -10.00638 | -50.25697 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8de9e342-fe88-34b6-8a4e-d7fb3a1d2a25 | -12.75567 | -44.91501 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57c606d6-ccdf-3dd0-9aa6-19664a1b88d3 | -11.28786 | -47.83578 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b5838ca-50db-391d-9c62-df54471e13f0 | -11.81508 | -45.03951 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efb7c484-ed74-3c4f-8ce2-f9b835750a3c | -11.90481 | -46.74211 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af1f5509-8bd2-333e-9c10-9aba899a4bb6 | -12.81188 | -46.91105 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba285e78-ff00-3dc5-8fdf-b8929c70ec16 | -13.77556 | -47.55339 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9561a3a8-07af-3011-8314-10f4e23c648e | -11.14288 | -43.40283 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 54cd6444-687b-36e2-877e-63b27955f6cb | -12.69554 | -48.5523 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8455570-0c0b-3bb6-a609-b4e6477abe8b | -13.76231 | -48.06422 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c484f83a-7507-392e-a02e-1bb0ef483836 | -13.97096 | -48.16746 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fa99b433-ff94-3115-aed5-e4966580e828 | -11.90928 | -46.29231 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba6552a7-c441-3676-b0f7-79de84ad480c | -10.90101 | -56.20104 | 2025-10-03 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18224c84-af85-30af-a0ac-50b1d3d0f820 | -14.19662 | -46.11209 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 52e193b5-f114-32cb-add7-c936eb9c9965 | -13.22604 | -47.3614 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aba2bb7b-1fb5-3e1b-b661-a570711eb710 | -12.82772 | -46.90887 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ca418f5-ecbc-3287-b920-6eff28bd106d | -12.75822 | -50.55563 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1fb59fd-b629-3848-a77f-1d67cf7f6360 | -10.34522 | -43.73252 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de27421a-35b0-33de-a839-173c53dec1a1 | -9.94506 | -43.74644 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 45baf429-305c-3e79-b688-08449cfc2522 | -12.23053 | -43.7673 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c5e6024-8e6c-3beb-9a7f-6a9c997cce7e | -8.61237 | -54.97575 | 2025-10-03 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 639876d8-25aa-3c1a-ac43-f23e03dca42e | -13.25347 | -48.42613 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f90c8ec-3907-35cf-92fd-e456298e96c4 | -12.6438 | -46.96663 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d918423-b952-35aa-95e7-9ecd35abcd52 | -11.45624 | -44.95712 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3bd428f-0b9a-31ae-b316-487cd3421ecd | -12.83244 | -46.94887 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0195c4d5-6729-3738-9111-8a631a27dbfa | -9.94338 | -43.57861 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28a70eef-6e8d-35a5-a1f9-f2640d0a9d4c | -12.30271 | -46.88058 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0dab847-4872-3ef5-9433-7272ea96c387 | -9.90178 | -45.95794 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2530357d-cd40-3422-b9e8-3030fada2635 | -12.83326 | -46.94411 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cd76564-87b5-389b-9cee-02cdf3a5d77d | -13.16712 | -47.88237 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36a80d74-bee6-36cb-8aa4-682aca9e0a35 | -13.51616 | -43.41285 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0140836-0228-35bc-820a-37d0ff183e4a | -13.75933 | -48.07103 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3387734-bc46-344e-913a-55598bde5f60 | -11.90563 | -46.29152 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c855379-02ee-3718-824b-f7ef2aab6ad7 | -11.49645 | -45.00259 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e38a7864-93af-3fa1-97fa-0bb3e82dbef2 | -14.44978 | -46.34134 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20046fcb-acf8-370c-ac1d-e2eac3c213ab | -13.33638 | -47.21393 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be93e5e8-7fcf-3073-b978-98550c77ddbb | -13.17008 | -47.88863 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ae70f3-7c66-3be3-babb-afd6ff5f0626 | -14.0116 | -44.96956 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ec5e719-7605-3eba-ac37-45a4b110595e | -10.29602 | -48.28751 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 406e2265-5067-365d-bd4b-0612dd40ea00 | -11.14355 | -43.37726 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 475aad66-2df5-3122-84ad-2043c2b68a02 | -12.38336 | -46.52038 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10dffcd0-31d8-3dfa-a1de-6e7c8942ec35 | -8.75964 | -49.93316 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b6dddec-4a39-3e1b-a738-c3c6ed8a7e82 | -13.19139 | -47.81461 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ede15a4-b6d5-3ead-91d2-4939109e94d2 | -13.96898 | -48.17836 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a46a7a8b-1707-333e-99b3-781f37fb791b | -11.83547 | -45.0029 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4abacf72-cb40-3bd2-a856-19c6e6c914df | -14.32338 | -45.87106 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5638538-8b6b-31ec-8179-f4d2fbc3012b | -11.62858 | -45.05205 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fe7de0d-b779-3cc2-ad28-5792bc0db8d3 | -13.51465 | -47.25589 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b63cd4-c9d2-30c4-b9a3-063dd810f966 | -14.21136 | -46.08937 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 060bf4f2-0b40-37c7-87f7-0d373951d981 | -15.0814 | -42.11646 | 2025-10-03 04:12:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d807360-300b-3d36-8af9-f70e3446c1ab | -11.56056 | -47.65915 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09b51529-abe9-3f51-a7e9-882d55b7ef11 | -11.90853 | -46.29665 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d2ebea8-6a54-3dd5-964b-f94c0fe8f760 | -10.34229 | -43.75064 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b50558-d044-3c62-9e01-c89cef01bdbd | -14.42553 | -46.35403 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6ec04f9-8f01-30b5-89a2-b568e0ad8971 | -9.45355 | -47.58463 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ce32252-73aa-305f-9334-08574d21a549 | -13.30995 | -47.59846 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b1b1c34-4937-34d2-8570-de9e90ffb779 | -14.42909 | -46.35474 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7aba65fe-d0cc-3149-b63e-327ed5c946a4 | -14.40893 | -47.87534 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59860b2e-2323-3942-acd5-6269403c55ec | -10.34033 | -48.18453 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3e73d89-458b-30b2-890c-d1d9cfbb6110 | -12.89989 | -46.89639 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6993b7a8-2f9c-3c9b-8f51-430c0b7e30cb | -13.69373 | -48.61625 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe4f3713-1710-39a7-8cf8-53486c4dd7a3 | -11.00935 | -46.63896 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04a5118c-66ee-322d-9d9c-7a076d85854f | -9.94227 | -43.74224 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd93ddbf-1813-367b-adfc-2c498ac63dc9 | -11.90439 | -46.30595 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b00b9ec-99c9-3cdc-8535-93fabbe4bd17 | -12.61419 | -46.98053 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b734a43e-f1bf-32fe-a9b8-d2e24732e8c5 | -12.81565 | -46.91163 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0417508-176f-33fe-bc9e-ba83697f70b3 | -14.42625 | -46.34982 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bbaa5c9-d609-3a2e-969d-bd654e7be185 | -13.20859 | -47.83207 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e04620c0-c6b3-3540-a0a4-b3e63dee9f22 | -13.21794 | -50.88182 | 2025-10-03 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa1514a3-78b0-34ea-9233-f2943a35e00c | -14.35664 | -43.85208 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| facb45b3-00d0-3f97-9633-af75d6ce68cf | -11.86857 | -44.99682 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea73181-0b2c-318e-b6f7-630608a3bf9d | -10.86332 | -45.4145 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9cfc4cb-4469-357b-9157-cd0d8dc9e1a4 | -11.79545 | -47.93116 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4229ced7-0221-3e1e-919c-2b5094daa914 | -13.30442 | -47.26286 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58e5721d-8e32-3294-a019-554f44712c07 | -9.48164 | -47.87305 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f640df0f-2db5-3dde-aa24-b500cb65a994 | -11.10351 | -47.83852 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e706e5d-aa1d-3969-ae82-66500dce5a78 | -10.24849 | -44.94717 | 2025-10-03 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df96cada-1b00-38f4-9674-4080a53029ef | -9.96001 | -48.7805 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 13899e06-6aa7-3f4b-8a02-1f3df1b1fd96 | -10.96917 | -51.08316 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f33e5ac-a69a-3e47-a6a3-7d4892743cb5 | -8.81548 | -46.66902 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ebab48bc-aced-3165-82ee-ba6860273d33 | -10.30031 | -48.28805 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 548f7414-1a23-35ec-90aa-8f1db60b8122 | -8.87894 | -50.89815 | 2025-10-03 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee7b180-211b-35df-a6df-6f2ef102b010 | -12.85459 | -46.93252 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed07e92-8c1d-3286-9944-c9923f3fd490 | -11.64812 | -46.86277 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86b16119-35e7-382c-993e-f5ad6fa6779a | -9.93943 | -43.58166 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 210081ed-e322-314b-a5ed-9b8fde6a3f82 | -12.30727 | -46.87663 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14f0f769-1cf2-34bd-b840-c9b5e0acdd29 | -11.13296 | -43.37911 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36516788-4390-3bf8-aca9-dcec73fb1fce | -13.28588 | -46.9893 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cba09880-f7ec-3e31-851d-2a1c3409f62c | -11.42631 | -43.48912 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4843a858-e1cb-3e2f-9ad0-aea32db3a71f | -9.03408 | -46.66927 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0984ee35-c7ed-37e2-b5c0-f8592b8f632d | -13.3568 | -47.33502 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb47deac-5620-3b5c-8a2f-020db811361e | -12.6303 | -46.95461 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 208a6787-dbcb-3229-92de-06775b3c6aaf | -13.12564 | -47.89528 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b4f180-6104-3f5b-9745-8dcf46d3ec84 | -11.80762 | -47.93322 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8020b529-554c-31b3-986b-25a2273bbe58 | -12.12222 | -43.43513 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README68.md)
