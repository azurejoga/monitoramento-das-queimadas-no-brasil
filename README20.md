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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ba0512-bf1a-391f-82e6-42ba69231b0a | -7.86975 | -45.35336 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15d687d1-e13e-394c-8af7-b6aa4bd98378 | -7.86577 | -45.34655 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38267c41-5e42-348c-a260-7b17893c3064 | -7.86417 | -45.35538 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 29d423cd-5c18-3da8-a1fe-be4cd476577f | -7.85982 | -45.35974 | 2024-10-17 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afb7ed16-5ad4-36c6-bad1-6f930cc1d3aa | -3.60688 | -44.79001 | 2024-10-17 03:47:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 727b8b63-158d-31ee-b7b1-42b22b9dc5b6 | -2.32023 | -45.07064 | 2024-10-17 03:47:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 963f3fe9-1340-35ed-8103-579fac7f3e78 | -2.31965 | -45.0741 | 2024-10-17 03:47:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dea42501-15e8-37b0-b8e2-7adf6dc314bb | -2.31905 | -45.07038 | 2024-10-17 03:47:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c392571d-16b8-30df-9280-005482f2e700 | -2.3185 | -45.07384 | 2024-10-17 03:47:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9f7e266-f339-34c7-a9f6-5a09245609cf | -2.3148 | -45.06971 | 2024-10-17 03:47:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184172e3-66b7-3c59-8013-54f9ab5fe462 | -3.60165 | -44.78912 | 2024-10-17 03:47:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abe3763d-d05d-3880-8a7b-91207e77bc00 | -4.77725 | -45.97626 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b05bb53-60d3-3100-83e7-ef95aa7d615c | -4.77169 | -45.97539 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6c3a14a3-4f14-33bc-80d7-1dfa8c004ade | -4.5908 | -45.74947 | 2024-10-17 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 829f39bb-c307-3b7c-a758-dab2e8fb0a15 | -4.59013 | -45.75335 | 2024-10-17 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4451687d-6a75-31f4-b436-6d5403de8a66 | -4.53537 | -45.77593 | 2024-10-17 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 601531f5-4ff0-3749-81b3-876dc4d313b3 | -4.53479 | -45.77936 | 2024-10-17 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 542b922c-39e9-3576-893a-038aefae179b | -4.40553 | -45.81141 | 2024-10-17 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f8cff6b-720a-32c1-9317-1f2a0265c1dc | -3.76184 | -45.75105 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73a4bcdb-7396-3daa-96d2-58f9edaa3a7d | -3.70538 | -45.91372 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 05e19a75-5f20-3d71-844d-14b148edcc36 | -3.70472 | -45.91759 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5584b475-9cce-3ca3-b4e4-3a7456e49885 | -3.70045 | -45.90876 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 519c702d-699f-3da6-a8c2-f892cb512c1a | -3.69911 | -45.91652 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c8989de6-93bb-38a7-8b29-459cd7a45612 | -3.69416 | -45.91163 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f85fff7d-b242-3cba-9255-9c3439b92325 | -4.78281 | -45.97715 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa22f9ec-be96-34e1-8b53-ec47065946dc | -4.78221 | -45.98062 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ef5b09-8ac2-3588-b39c-782191209509 | -4.77784 | -45.97286 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ed9ac5fe-1209-3037-be98-32df63598216 | -4.77666 | -45.9797 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c40387a3-71d9-3a7e-9a58-050eadef1240 | -4.77107 | -45.97892 | 2024-10-17 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d9e4eb40-2b5f-3ed0-85db-3874fd45f497 | -4.73407 | -45.70226 | 2024-10-17 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07cc11a7-6779-307d-97f0-675de763b4a5 | -4.72855 | -45.70166 | 2024-10-17 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b07091a6-737c-31b1-9ab7-dc998871ec65 | -4.40618 | -45.80757 | 2024-10-17 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4d545cf-e661-3830-a50b-ccdee4c80e30 | -3.76122 | -45.75474 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af796281-d12b-343f-8597-2812f3135662 | -3.69979 | -45.9126 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 43b8c18b-b42d-370e-b643-d84d75027771 | -3.69844 | -45.92044 | 2024-10-17 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 01f27e69-33f4-3c69-9cc3-e6660970872c | -7.85241 | -46.25188 | 2024-10-17 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e46fd7cf-4f1d-38a1-8abc-f9ab28c88fb9 | -7.8518 | -46.25525 | 2024-10-17 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02642fe8-f121-36ab-a03e-1e12329318fe | -8.29183 | -45.99109 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29bed6f1-e847-3a6a-93a1-ac3357dcc6b7 | -8.2879 | -45.98742 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24f5fcd-b0a9-3c41-978b-5d8a51008a6f | -8.28264 | -45.98659 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21344d41-a381-34e3-a5f1-6f70ec49ddf5 | -8.2819 | -45.98622 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9daf2a56-84ee-3f52-9c6a-afa287b92743 | -8.27722 | -45.98224 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2220b97-d3c2-3032-8f0a-47b5d9d298a3 | -8.27265 | -45.98191 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d7c0855-cbb0-3ad8-8655-0cae1f30632e | -8.21649 | -45.78641 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c59ec35-9922-3f01-b9f9-debbb37abccd | -8.21593 | -45.78948 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5cff0a5-4e69-3921-8dae-8911c0573dac | -8.41253 | -45.70829 | 2024-10-17 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f28f0c5-fdbf-3af2-b874-2d61f3a1587f | -8.29241 | -45.98791 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 682d8c6d-ea1a-31f6-b627-3d8e0c73419c | -8.28716 | -45.98702 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1143e25e-48b8-307e-a767-771a1acbda85 | -8.27794 | -45.98259 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cd57e56-1797-32d6-b057-9dd5fdfd9a09 | -8.27737 | -45.98583 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 820a1d87-19db-3e95-8af0-0ca8bd481770 | -8.27662 | -45.98549 | 2024-10-17 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7152652-c5db-3336-a245-4a6564b10f5e | -3.24989 | -46.87902 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 720696a0-6843-3141-8b80-14c7050a6a69 | -3.24915 | -46.88336 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52ca5d74-3123-311b-812f-ef3ff7908c3f | -2.65956 | -46.05168 | 2024-10-17 03:47:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d12999-fefd-3173-8a0e-55cf0d89d679 | -2.65381 | -46.05057 | 2024-10-17 03:47:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efd4c997-5781-38f5-bc22-183a486966f9 | -2.37391 | -46.48923 | 2024-10-17 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 817ef037-23c8-3ba8-865f-1c69da3b85d4 | -2.36795 | -46.48822 | 2024-10-17 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6cb7742-9a8e-3a79-8594-089cae58848a | -4.31894 | -47.71128 | 2024-10-17 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520235cd-72ca-3e24-af5f-29c4491fdbc3 | -4.55454 | -46.67484 | 2024-10-17 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d9b74223-e8c8-3f48-878d-98e9cb620665 | -4.5538 | -46.67906 | 2024-10-17 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ba37f31-cd49-386f-8776-138ee2835750 | -4.54799 | -46.67796 | 2024-10-17 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47418c2c-d242-3724-b67a-a981d8e05c1c | -4.35774 | -46.82201 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e97d1a45-38fe-3cdf-a4db-b53118ce4a84 | -4.31976 | -47.70652 | 2024-10-17 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a52b8a-b167-32a0-830f-9b79c9f5e8ef | -3.95372 | -46.43834 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1bf7d69-8421-3a32-8b4d-c4e3a5f3ed43 | -4.6565 | -46.2893 | 2024-10-17 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c55c1f9f-b8bf-308d-9449-b9ab32781b00 | -4.65583 | -46.29321 | 2024-10-17 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b9de328-99ba-3b56-8500-dfed2ea9898c | -4.54869 | -46.67391 | 2024-10-17 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a2448f43-e924-3bf7-83b2-e97a7b55fe58 | -4.36434 | -46.81897 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f70cad2-151c-3ca3-91cd-7207b34d8217 | -4.36361 | -46.82325 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 086f9ecd-bfd1-33da-a247-036bc6ead3be | -4.36239 | -46.81719 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba0838ce-ec8c-3029-a5c4-2380bc2b8e84 | -4.36164 | -46.82145 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb025874-bdef-3f10-93dd-93f9637824f7 | -4.35848 | -46.81766 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa66601c-58af-3c20-aac5-bca18be32219 | -3.96008 | -46.43602 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0144b91-02bb-33b3-8f57-e98df581f3a5 | -3.95438 | -46.43446 | 2024-10-17 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a489da-58f9-3eb1-97a9-b26b8f71f5fe | -1.87614 | -47.81124 | 2024-10-17 03:47:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90987464-f9bd-318a-b0c2-e243d9ebee9c | -1.86964 | -47.81005 | 2024-10-17 03:47:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f89038d-c4f9-3d3c-84fb-39e8ef710183 | -3.70184 | -47.62155 | 2024-10-17 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3a6e1b-9abe-3f43-bcb0-cf3cdf8488e5 | -3.69562 | -47.62016 | 2024-10-17 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1e686ab-973c-3c6e-a353-210e765fa005 | -3.46814 | -47.66866 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18f3802f-8a4c-3bc6-aee8-556ef1b5428c | -3.221 | -48.9187 | 2024-10-17 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cfa3a0ae-4de5-3cd5-a13c-0c243268eab7 | -3.21993 | -48.92492 | 2024-10-17 03:47:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2681c2d7-eac3-3345-a6e1-9dba51a0442d | -3.69822 | -47.62164 | 2024-10-17 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69de87e5-5b5f-37ac-b793-eaa1cb9d917d | -3.4698 | -47.67184 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fb04879-e865-3cad-ae45-0bdc40e631fe | -3.4673 | -47.67363 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b26a8ca-b218-332b-a622-7f54b82877b4 | -3.46347 | -47.67085 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73e8f407-ea20-35d7-905b-ba23e9a42ab7 | -3.25605 | -47.97796 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1224a2a8-e6b2-3f57-8c5b-2c54f9850abb | -3.2551 | -47.9835 | 2024-10-17 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af994c0e-1006-3657-bde2-e2499156ed2c | -2.96823 | -47.9926 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39bff47a-d2b7-363c-9caf-fea049e443cf | -2.97471 | -47.99373 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3c24a11-df63-3f18-be52-d9eb93665887 | -2.9738 | -47.99909 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b91306de-be57-397c-ad8d-6ca56e2190dc | -2.97291 | -48.00437 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e5adcce-fced-348c-87fc-cf6841e8f888 | -2.96731 | -47.99801 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2ab1a4d-c2ba-3056-87ec-986670394310 | -2.96642 | -48.00326 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c73104f-4148-333c-95a1-69f01b8009ab | -2.96551 | -48.00864 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 027d61db-f771-348a-a226-a5d100604263 | -2.96175 | -47.99144 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 431520f0-646d-3d2c-8fcf-861e406ea4dc | -2.62973 | -47.63354 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f40a07db-bbc8-3fdb-9778-81be0f0ea790 | -2.61161 | -48.25723 | 2024-10-17 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9ae6b943-4ca2-342c-94d2-399522f36b15 | -2.61066 | -48.26292 | 2024-10-17 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2d9df1c1-9d34-3a18-9263-dc60dc4cf96a | -2.60498 | -48.25613 | 2024-10-17 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c60b2522-4f46-38b1-b9a5-5f19ec8c9ad9 | -2.60404 | -48.2617 | 2024-10-17 03:47:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |


[Clique aqui para ver as próximas entradas](README21.md)
