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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfbc3666-99ce-34e5-9fd8-f89a48c185c9 | -11.46138 | -47.31345 | 2025-08-08 04:59:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ffc0b8e-c418-3e75-a145-82c4bee2d95f | -8.91034 | -62.43425 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d690b0c9-9bcd-31f7-850c-a32aa01824bb | -11.73737 | -45.02602 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b311c114-d208-3d17-a28d-4e93b22b049e | -11.56491 | -44.85505 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 586ad6a3-cd86-3425-aec3-50ca7aa30f8a | -10.53478 | -42.55138 | 2025-08-08 04:59:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| df2549c4-60aa-3af2-97d8-1a2de0d9f2d3 | -8.06616 | -49.71378 | 2025-08-08 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68867c03-276b-31d5-a4a3-558cf5ec693b | -5.88026 | -57.74605 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4f7d980-4a4f-36a9-8b56-e4e7f06d24ec | -12.0921 | -44.73384 | 2025-08-08 04:59:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ebc02a-b979-3128-9d9e-f350d6406b6d | -5.87962 | -57.74752 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab75881d-7dcd-3a85-b3b3-e5786d541fef | -10.43217 | -44.35062 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb727f1c-612c-3bfe-a64e-4e31885691fc | -6.28814 | -44.22344 | 2025-08-08 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c4a311c-1540-37e9-b152-95082d9861fc | -6.15206 | -55.80643 | 2025-08-08 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91f302be-0766-367d-8541-8d918a2125a9 | -11.57071 | -44.85575 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c171f1e-700d-3a8a-a2c5-34a333403f18 | -7.25141 | -44.66217 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f96958a4-19c9-3cc4-8634-bf2d47b5ca38 | -5.0032 | -56.03826 | 2025-08-08 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18607cb6-b028-34c9-b135-ed5afb405c69 | -10.43387 | -44.35755 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453ea8a1-6cd7-3e6a-9080-73a1596348f6 | -7.04597 | -59.19072 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fd05c4f3-a990-3b00-b208-fa0847c67139 | -5.80973 | -59.22725 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32f2e369-a91b-3515-bd75-4b134c8388a5 | -7.11205 | -44.20846 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 178bdb50-210e-30df-9350-9eb15a68ec43 | -7.38369 | -44.24323 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e73292-3a3b-3d28-b485-6f0e725f32aa | -10.62885 | -44.76278 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9c695637-fb64-3cfc-8b3f-e5092ba53525 | -10.8285 | -49.37794 | 2025-08-08 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8291ea41-ad22-3e7a-8ab7-f6cee983e9c1 | -7.04654 | -59.18724 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d95c2a37-e584-36cc-a955-6ff0ce6437e0 | -7.05085 | -59.19239 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1369a757-6c5b-3753-8ac2-258df83cf70d | -6.4153 | -53.37753 | 2025-08-08 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ba2534-dfa4-342a-a821-ac6b427c0199 | -6.81137 | -44.76707 | 2025-08-08 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82f65fa3-5e19-36c6-87cf-4d9a0ecd61f1 | -9.5558 | -47.88107 | 2025-08-08 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 622342cd-7c4f-3eb2-a3eb-ef9914f91856 | -7.06449 | -55.41261 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ecd1d4-e776-389f-a4f3-13cf03cfaad5 | -7.24539 | -44.66488 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 888254c6-01d4-3cec-9786-28ff3f1a2b38 | -9.20036 | -49.65789 | 2025-08-08 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c382f9f0-5660-3eca-8906-6bd42edbf6a6 | -7.26698 | -44.32 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b9ab55d-958d-33d9-9a26-e1d8bbaf6231 | -7.89462 | -45.33529 | 2025-08-08 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7b4766-22fe-3194-bf01-475aef12f740 | -10.62309 | -44.76196 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54523608-231a-3ceb-bf3d-38b91053d037 | -8.92037 | -60.74389 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c48bfe-de61-3cbc-8eda-7fb260a9e82e | -5.81322 | -59.23169 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f667df66-083b-3cae-8d9d-f0d4601565f4 | -11.46066 | -47.31905 | 2025-08-08 04:59:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8116110-f152-367d-89e6-ec1758d36a99 | -5.81793 | -59.2287 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8f7a91f-acfd-34e8-bab7-ecc3aeb5d255 | -11.65468 | -46.87262 | 2025-08-08 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1b91bdd-44a0-3121-b699-0f93c0d17570 | -6.28761 | -44.22718 | 2025-08-08 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cad5246-b22b-3a24-87ff-b34c9421c40a | -7.91583 | -45.53675 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e43549f8-7ba5-3a74-8663-00cf51a8d9a6 | -7.38183 | -44.65425 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04355809-6bed-372a-9a73-662bd9edb20a | -8.92539 | -60.74052 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b9623fe-22e3-3300-85cb-a99c26be52a6 | -10.43332 | -44.36185 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10d5af71-853c-3159-9e36-0d647a8ccae8 | -10.62936 | -44.75868 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ddef62f-c388-3da8-bc82-dbc6cd47ec3c | -10.63512 | -44.75943 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5b01b6d-6340-3731-9c14-ff846319c779 | -10.61157 | -44.76038 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b493480-f500-38e4-b6a9-cafeb1d7e269 | -12.0985 | -44.73042 | 2025-08-08 04:59:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8f37223-494c-3e68-94ac-9e92f4b87353 | -11.02626 | -45.06826 | 2025-08-08 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8ce42a6-9ed4-3528-9b66-7a0fa6372682 | -7.10953 | -44.22692 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ca6ba8-5c81-3d6e-8bac-98561f2580c0 | -7.37677 | -44.64989 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff903430-6061-3cf5-96fb-9e23162dd15b | -8.1088 | -47.43282 | 2025-08-08 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4640a078-f6b9-3ac4-a923-fa724f504f50 | -7.91628 | -45.53348 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a74adf-68f3-3a12-aab7-32a5c611b077 | -11.74426 | -47.50557 | 2025-08-08 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a6c4107-03a9-386a-92bc-d5febec0e1ef | -7.1162 | -44.22055 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2a12c0-45dd-390c-b032-434a3cefff89 | -6.91313 | -52.84831 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48341d4d-9f66-3246-add5-d2be877b806b | -5.81445 | -59.22425 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45cace93-19b2-38eb-ad75-574acf457891 | -7.22985 | -44.65457 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1e2cfda-4fc5-3fb2-96a0-328602a1d3ef | -11.02676 | -45.06425 | 2025-08-08 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7031f340-381b-317f-8525-4127c3002425 | -8.24892 | -45.06954 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a23c069-3988-384b-8956-e98300fef14f | -7.24638 | -44.65761 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67d8ea87-afa1-3449-913d-2455fe56db86 | -7.75072 | -51.13591 | 2025-08-08 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a3fd227-6b73-35c9-ae4b-b8fdee7627aa | -8.52767 | -43.31325 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfd32a38-bfcb-3978-af6c-b441b27762a2 | -7.10381 | -44.22639 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb25e78d-2c9a-3daf-830b-ab532bbd2491 | -8.21064 | -45.0633 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8709d5e0-2577-30a7-b2c0-dd5a13db1129 | -7.91402 | -45.54982 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c72157a-8917-3705-9816-945dfc418268 | -11.74703 | -44.94946 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58051ab6-9624-3b64-9727-d958d5241d9e | -6.96374 | -42.86404 | 2025-08-08 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 991258ef-51ee-3b2e-b232-a6b83731f683 | -7.04711 | -59.18379 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9066431e-41d7-309a-a3f3-017ebaef823f | -9.65322 | -43.84597 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7d0aa927-7379-3fcc-b69f-4327c3109fde | -12.09797 | -44.73467 | 2025-08-08 04:59:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e240f965-78c5-35db-9cae-e42b904c33d3 | -7.26911 | -44.31837 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca4ae13-435c-3d2f-8309-ca7ca45d84c5 | -7.25498 | -44.59407 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccc1ee3a-66e2-341c-93d4-605aca3fa7cb | -6.41863 | -53.37804 | 2025-08-08 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04d087e6-9027-3577-8f1c-9a5eb4720ab5 | -7.06113 | -55.41208 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1213871f-369e-3b49-be73-9b0a6005fc4b | -7.06056 | -55.41566 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b843a26-3362-3136-9158-3c9dc972471b | -7.91493 | -45.54325 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 265931bd-b64e-39a9-a0e4-0b128288c69c | -11.74737 | -44.95181 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4bcc318-b322-39a4-b488-280282ad84a2 | -7.37628 | -44.65348 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 54dbae12-9dd6-3f6e-911e-11585d749589 | -7.80776 | -48.38055 | 2025-08-08 04:59:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369fa611-70be-34f4-b1d0-f66cba4a8696 | -7.25042 | -44.6694 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c7dfb7a-741a-316f-866a-8762a1a4ee89 | -11.07365 | -48.35794 | 2025-08-08 04:59:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7f6bf11-87d5-39e1-88d5-6d9b388fb9a3 | -7.22593 | -44.65143 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 569d4037-2b9c-3c1e-952d-0a313029de75 | -7.81925 | -46.88365 | 2025-08-08 04:59:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 300cce77-5a08-3b29-baaa-941657471b26 | -8.92397 | -60.7488 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddb5ade4-866a-3947-92d2-69c4b4922619 | -8.06939 | -49.71944 | 2025-08-08 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008cb4ba-9877-30a4-ac76-039e0872636f | -7.04309 | -59.18315 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 815eca71-c66f-397b-bfd8-1a6998990628 | -11.75272 | -44.95087 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9ecc33-c7b5-3c17-8e6b-4e3c99cfd7fc | -6.12899 | -42.95953 | 2025-08-08 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| aba545e4-72bd-3700-a14b-ae7eb4a9e44f | -10.52817 | -42.55046 | 2025-08-08 04:59:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6e9f1357-69fc-3172-b28a-1cb58cb84129 | -7.37122 | -44.64909 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9046ead2-3c9f-348c-9ebe-8bdb21af1a60 | -4.99787 | -56.04913 | 2025-08-08 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1baed334-8997-3195-a2bc-564a8109c967 | -8.19858 | -46.98698 | 2025-08-08 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d86bd958-3de1-3cfb-8e4e-f15a23b5c625 | -7.38579 | -44.24213 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a7e09db-3fab-31d1-9e4e-798e830f6f2e | -8.91966 | -60.74802 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be9c1d24-2d41-3533-ae34-ecf30e301fa7 | -11.74603 | -44.95742 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31128b64-3c0f-36f0-9c15-214ce066602a | -10.61733 | -44.76117 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0803e045-c822-3e6a-b427-0ee08d7c040d | -9.65267 | -43.85018 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ff4dddc4-ae20-39c5-a9dd-7b9c6f80db2a | -6.92918 | -44.68711 | 2025-08-08 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d450a6e9-5288-3a68-b34b-7041009d2a8c | -10.63712 | -44.74333 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96a25b29-ddd2-35fa-9198-233531abeb78 | -8.90564 | -60.54852 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
