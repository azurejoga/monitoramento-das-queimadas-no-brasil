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
| 23319c81-5296-32ab-a6d8-653902618ad8 | -19.09971 | -50.45546 | 2025-11-02 00:50:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.3 |
| ce9173d7-1816-349e-b80d-e01d483d31d1 | -12.16059 | -56.76996 | 2025-11-02 00:52:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5c15f602-ea47-391d-98fb-3419aebcbf5c | -12.23762 | -60.32466 | 2025-11-02 00:52:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c381e814-5ca9-30a9-8fd4-191a730eb43e | -12.17181 | -53.62922 | 2025-11-02 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0f8f2cba-2006-3f1d-812e-befde3241b33 | -10.9766 | -54.24546 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a7ac0362-c7b5-3b15-8dd5-2cf48190ab71 | -10.61283 | -52.18499 | 2025-11-02 00:52:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e616cc0d-68a0-30b2-9e24-3721e8e847be | -10.97784 | -54.25443 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a6fb71f-588e-3485-976e-3a6232dc59da | -10.30274 | -53.77458 | 2025-11-02 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0efb818d-4878-3fc8-b260-a162a438b211 | -11.20313 | -53.81969 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4c38d83-3eac-3e8d-8d32-1c2e579d14e7 | -10.62207 | -52.18361 | 2025-11-02 00:52:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3b43f594-e6fa-3612-9ef6-1d5e7773ce25 | -11.36311 | -54.31193 | 2025-11-02 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b252deb3-837d-3b09-a789-f3f36fc98bbe | -14.45332 | -51.529 | 2025-11-02 00:52:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 25c520dc-3a84-3cc8-83bd-c426cbba1439 | -14.45475 | -51.53878 | 2025-11-02 00:52:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 019dca4d-7cbb-34ec-836d-ecd320a17cd8 | -12.88028 | -50.86915 | 2025-11-02 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a843e987-cb5c-3922-aa4c-8636dc7d48d6 | -13.98064 | -51.5131 | 2025-11-02 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c2c87ebe-c53a-389a-bcbb-7ceb9abb63d3 | -12.37609 | -63.90543 | 2025-11-02 00:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4c998053-ff9b-3f54-a267-a823029fbfef | -12.37208 | -63.86595 | 2025-11-02 00:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 80a501f0-fec6-3cc5-b3b5-253b44c30acb | -10.78933 | -56.82028 | 2025-11-02 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fd48d2e9-feee-3454-a6ed-d19bbcb6c292 | -10.62347 | -52.19339 | 2025-11-02 00:52:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1f5cf57a-445b-3363-81cb-fed10a7ab6fa | -12.25017 | -51.33243 | 2025-11-02 00:52:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d2e5255-94ef-3590-b1b1-00259a87d39a | -12.43758 | -63.1454 | 2025-11-02 00:52:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 09dcaec1-0424-3b43-a597-59f6f5452585 | -10.78791 | -56.80944 | 2025-11-02 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 755f052d-e7df-3bca-893f-0db21e81b4cd | -10.99988 | -54.0075 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2153a113-e939-32c0-8f53-b3a738516248 | -12.17056 | -53.62024 | 2025-11-02 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e01970d3-a1af-3c45-b8ea-9f05cf670ab8 | -12.36908 | -63.87298 | 2025-11-02 00:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| d3d2addb-2664-3a82-adf9-cb4849bc1ef5 | -13.97919 | -51.50322 | 2025-11-02 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ecad6fe7-5f54-3ecf-b44d-201270c7ba04 | -10.99864 | -53.99855 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ba03c45e-70be-3965-a970-5eb1224767f2 | -14.02469 | -43.49451 | 2025-11-02 00:52:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 6c241e02-6026-31b7-a9b6-cd11a08ea522 | -12.88189 | -50.87996 | 2025-11-02 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1b26b085-6fdc-3529-8ccf-7c41f2275d6e | -10.63129 | -52.18219 | 2025-11-02 00:52:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 07853b66-0ae8-3571-a06c-883e2a756e17 | -15.62931 | -58.23369 | 2025-11-02 00:52:00 | TERRA_M-M | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3174d4f0-69ee-39b2-8831-3edd4cf634ae | -10.77962 | -56.82158 | 2025-11-02 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| deefc0ac-b263-3663-9ec4-af2d83eac75d | -14.01826 | -43.45854 | 2025-11-02 00:52:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f0d204fb-f028-316f-8bd8-8a84be9b55b5 | -13.50152 | -56.5684 | 2025-11-02 00:52:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 71825884-34f0-3e49-a7f1-60dc95bc30f7 | -14.03079 | -43.48831 | 2025-11-02 00:52:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| f846ad3a-15a1-3d74-9733-7095eec344f8 | -12.41845 | -54.49073 | 2025-11-02 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f90a92ed-92e2-38f2-85e6-e7dfd0bd1fcf | -12.23613 | -60.31939 | 2025-11-02 00:52:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 60d64286-037a-38aa-8a25-9d4e4a819a1d | -10.7782 | -56.81076 | 2025-11-02 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16251390-4279-3bf5-ad49-f8293f61ece9 | -10.98981 | -53.99984 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c1bba9dd-9382-39a3-82ee-19d4cc270e90 | -10.99104 | -54.00879 | 2025-11-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c89d192-19a9-3410-9fe8-7279ab2da9ef | -3.70714 | -53.38105 | 2025-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eea20e82-94b0-316f-95b4-e30227d67298 | -1.24695 | -53.84516 | 2025-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9f471e5-f436-3df5-a25f-b5bc3da2f9f9 | -4.2949 | -45.88503 | 2025-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e19d84fc-5ec9-3972-b698-0dc72ba8639c | -3.22419 | -50.57857 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1984ffb7-b397-326a-9f31-24a6f905c6d1 | -4.51041 | -50.49901 | 2025-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7ccfbc80-551f-3c74-817a-e886b3162b03 | -3.56366 | -50.15656 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 51a051de-f0a8-3c81-ba48-687ce85160a7 | -3.24268 | -50.79243 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7078ee21-51c5-34bc-8ab3-0500b4f78539 | -3.31835 | -52.55972 | 2025-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6afdf0f6-6d3a-346a-ade2-2e86ad79d61f | -3.58491 | -47.52713 | 2025-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 96be3a2f-cca5-3f9c-8ee6-d1132036ed32 | -3.55841 | -54.56433 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cec1b8dd-7b33-3822-91ab-1ec2526be94e | -3.61887 | -51.4663 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 990b38e5-2386-3d92-83bb-38696c1aa504 | -3.02972 | -51.23771 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a0488788-3acd-3e42-91bc-519af56d3cd2 | -3.58321 | -51.55712 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1cc890d7-83b4-3d01-a7fb-57f0038c8dbd | -1.97341 | -52.10624 | 2025-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 82569acb-0325-3ab6-941a-7ba4aa74b237 | -3.08073 | -52.91871 | 2025-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d2c1721e-3bb8-3d84-a4c4-b1934404d715 | -3.83201 | -50.49386 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5279d318-78e1-3fc2-b033-2f9d522f2331 | -3.65693 | -50.71664 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a6253dc7-1833-3c11-9270-cae8b972237f | -3.51932 | -50.31814 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 64d86f98-4c07-34a6-ba34-5801ff7c01f2 | -3.50521 | -50.46519 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e1ca1cef-a28b-3729-b626-59c2ef4a2aa3 | -5.56881 | -52.1243 | 2025-11-02 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bceedbe4-c3f2-3f71-8fd4-315d894d23c7 | -0.68527 | -52.38197 | 2025-11-02 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef605763-c87d-358e-b625-79633c0f4768 | -1.26288 | -54.55604 | 2025-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 196af765-552c-3bdd-8c45-3505513c2ea6 | -3.55185 | -50.15825 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ca1094ca-56da-3099-96e5-592bcf0c5643 | -4.12423 | -49.15692 | 2025-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 069c86a5-bf0d-3507-9505-0a3531496066 | -1.73773 | -54.45776 | 2025-11-02 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 388a8dc4-703c-3bca-80ad-3c8b118a5239 | -4.59303 | -48.69784 | 2025-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8a59736b-d4dd-3f4f-af3f-005729f29626 | -4.1272 | -49.17035 | 2025-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 13bccba3-152b-34de-8ec0-b68a1f621e38 | -3.65479 | -50.70185 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4c562684-05a3-31a0-ae9f-23d01b6a4d58 | -2.83822 | -49.41441 | 2025-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d4ee2d8d-3592-3056-bf7c-4e71ec71fd6a | -3.31778 | -52.56558 | 2025-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 11e21ee4-6417-3ee6-bfdb-94e1f329f91a | -0.68353 | -52.36946 | 2025-11-02 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 08126c94-c7cb-36e6-945f-4f43f980a923 | -1.26417 | -54.56536 | 2025-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a28fba2-66c1-3ccc-9059-b14723da0c12 | -1.96721 | -52.11296 | 2025-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 695705ac-26dd-36e3-90d6-41c45c1d1f64 | -3.382 | -52.36612 | 2025-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4938747d-33f8-3b8e-84e1-930fc050bd6c | -3.89712 | -52.1011 | 2025-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1fb9a1a4-2d53-3f72-985c-ef5245ca62c2 | -3.56218 | -54.59138 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89379caf-7447-302c-bc6d-242e3f235c7b | -1.73902 | -54.46709 | 2025-11-02 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f553350-1162-3b5e-b14e-7c39cbe73906 | -3.01173 | -49.43589 | 2025-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| c15686e0-426c-311f-ae1c-339347b7e930 | -3.70575 | -53.371 | 2025-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9b5cbec6-6cb3-37fc-86c4-8fc5e87938aa | -3.28361 | -51.61861 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b23fa7a0-e83a-3e2b-afc5-a4f89f539575 | -4.13372 | -51.13723 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f103eccb-15d7-38c6-bc52-6dbc4304c972 | -4.59266 | -48.68244 | 2025-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 46c49edd-9657-3297-8003-ac73242785fa | -3.0139 | -53.96514 | 2025-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f184bb2-ef8b-30cb-a840-3e18421df2b8 | -4.14648 | -51.14897 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3716b599-463d-393c-adc9-37ad8d04b183 | -1.9648 | -52.12008 | 2025-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 750db607-186d-37c2-9ec2-014adc5080cc | -3.56093 | -54.58238 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 153564fe-d6fa-32c5-8fff-f4d492859d24 | -5.75372 | -53.40179 | 2025-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bdd92df5-74b2-3a18-9625-fa29036ba273 | -3.50748 | -50.48066 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 28c5d036-4bd4-3d06-a22a-2b9c349ca6f5 | -5.27851 | -50.96231 | 2025-11-02 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13bae34f-23cb-33c7-9d0d-5c21d2553041 | -3.01451 | -49.45501 | 2025-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| c2fa691c-dd56-3819-a5a6-b21648983099 | -3.45595 | -50.21194 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f6e3189c-93ca-3529-91dd-a7d35ccd0e79 | -3.22392 | -50.58873 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 025e79fc-25e9-3012-bbc4-39ca35bd18b7 | -4.71926 | -45.68241 | 2025-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 76e03dd2-6e06-3504-9b61-90c9807655f2 | -4.50916 | -49.79451 | 2025-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f91c7fa7-71d8-3d4a-ae28-098ec806c6fe | -3.32982 | -52.56941 | 2025-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46090a66-439d-30af-b8e1-4ad912f557be | -4.1357 | -51.1506 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5ebbb118-fa95-3771-a914-7ad2d6b408de | -4.13263 | -51.15755 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 593cbfd8-0808-3496-80c5-02c19aaf35c6 | -3.62079 | -51.4793 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 633eefc1-8919-3f76-81cc-1a4a86224e67 | -3.24174 | -50.78686 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7bde6b24-c970-3fff-bcc3-bbdf1c9c7645 | -4.72459 | -45.71646 | 2025-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |


[Clique aqui para ver as próximas entradas](README3.md)
