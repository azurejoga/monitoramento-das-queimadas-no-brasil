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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f1f6757-59da-3692-8967-1ebf967fa19c | -5.69998 | -53.63956 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38728f57-afa9-3eec-b146-3e7ec2edbf9f | -6.21936 | -44.4311 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d484eece-ac93-33d1-b0ef-69e5844108a1 | -6.20544 | -41.75554 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0cd9f2b2-4e23-3068-bbc0-11d162849069 | -5.69487 | -42.67931 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b80fe525-225d-3e09-b632-15b3670d1925 | -8.16423 | -43.3064 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e97c1304-1c50-3330-9aca-1b616bc08d54 | -5.60447 | -42.69585 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 464edb96-9899-34e7-8809-5736158ca4c8 | -6.12232 | -44.85665 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a4974e0-dccb-3f56-9070-6a7bc7af2436 | -6.23067 | -43.02521 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 501c02b7-1de7-395e-a879-d724176ecdaa | -11.09431 | -45.87525 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 128fe530-145a-33b7-8ea2-73e84bacb575 | -5.24907 | -43.60606 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b51b3781-7ac2-3ad7-b255-87fe2e60d164 | -9.10247 | -46.67311 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7914503-697f-3be3-9fed-94f1a5ee1504 | -5.27133 | -43.26529 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a0e8a9a-d35f-3088-89a2-826e81e6184e | -10.65836 | -45.29002 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 554a8cfb-4b66-32e5-acbe-80e3923c468d | -6.13147 | -41.76542 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7f96be6-4826-31a3-9bee-cd8dede61c1b | -9.72816 | -44.51036 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8fc210c-fcc1-3038-89fb-793f7be17333 | -6.37002 | -44.70932 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaa45a58-5aaf-353b-aab6-9e9d6d6e98b8 | -11.09761 | -45.87578 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e3b2035-1f92-3706-854c-08126a0d7eb9 | -4.81029 | -45.73094 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d213f6e-c08c-3448-aab9-6432546c799f | -4.8646 | -44.43532 | 2025-10-17 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66a0fb46-8e55-37a2-8c93-e0f5ba1a48ad | -10.10236 | -44.57624 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da290da5-54cb-3c07-b2d4-0252d7c9a49a | -5.54804 | -41.33447 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6352a58f-3a41-33a9-b326-b8b57d912051 | -5.88668 | -43.90499 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55f61a11-4124-3926-8b01-b07783eeb527 | -8.28887 | -43.38522 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 134b40cc-47d4-386f-a196-f877602d6119 | -6.64792 | -42.298 | 2025-10-17 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16729e59-cd43-3db5-802b-c8f88f54ae04 | -4.25828 | -48.54971 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9319001e-f597-3128-a7a0-05486a8b5d27 | -8.45273 | -46.24203 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cc78fa1-5696-3661-9ff6-6da1c65e71bc | -5.55422 | -46.95123 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35b76cd3-969e-3768-ac61-857a7358e32a | -10.51017 | -43.42019 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87a081b7-0da7-36f5-b688-03b1e8279f4b | -6.16188 | -41.70786 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1d83539-5589-3805-be88-f28bad45c707 | -4.58276 | -46.30505 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9586d91-bb84-3f38-8e62-3ad000575f30 | -6.58835 | -47.0722 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d273c4f-df63-3c69-bcf7-dca0c040db29 | -7.4114 | -44.75447 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c759c2c-d32b-32dd-8c0b-55595cc907c9 | -7.79548 | -44.93271 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb842dc4-90ca-3925-9708-172cb1317174 | -5.71855 | -43.82562 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a3ad23b-83f8-34b8-9c27-e7bd058bd8e8 | -7.95752 | -44.15086 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13a5a48c-1be7-3877-bd1b-abbddc26f0ec | -9.71225 | -44.54762 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67ed83eb-dc78-3d6d-ab05-ba140d05cfb2 | -11.00765 | -45.25614 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cbd68dc-011b-35c1-8cb8-e0c1a1d0b314 | -7.75929 | -42.45407 | 2025-10-17 04:19:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92757dea-9958-30ca-929c-3b4d9fbdd5e9 | -10.35797 | -48.05222 | 2025-10-17 04:19:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06edf6a2-5920-3fde-9ff3-1667989edc0a | -5.57571 | -41.32161 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25c6c7aa-a0bd-3fc5-9922-f5ab07ca4b09 | -10.26338 | -44.03301 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 66dd4c89-8fca-33c4-ad45-859a469d8a15 | -6.40493 | -41.89758 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3eb27301-df11-37e5-bef4-29efabc5b34b | -10.27348 | -44.03461 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08a3c147-91f7-37b0-acef-b3a16054aab6 | -5.88883 | -43.89111 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5725477a-38fe-3e97-9d6a-5649a48c4024 | -7.16607 | -44.99502 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b172bb85-cf61-3463-aeab-ac6c9c04f44c | -4.86131 | -44.43481 | 2025-10-17 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fb660a8-a8b1-3483-b3c5-4cd2afc2d41e | -6.30175 | -45.5323 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4198757-2f43-3844-9c9a-678c3bd7fddf | -7.96968 | -45.14077 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65641269-3d19-3c25-a49c-da7ace61253c | -11.47238 | -44.19854 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e361f094-ade1-38cc-a3bd-c051bfdef470 | -10.50502 | -43.43095 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e6489051-e407-301b-9cbf-1208811fec54 | -7.27998 | -41.95195 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| baaa24a7-a5e6-30dc-837c-7ba6624b355c | -10.10301 | -44.61609 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87bc602e-5fe4-3d93-ab02-27217a717b43 | -10.50382 | -43.41555 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ac216b-3dfc-3bf4-b394-6159c9ac19cc | -6.53599 | -44.34361 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9979bf8e-6389-334e-821e-398562a7f1fb | -10.84403 | -43.9489 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1a1258f-fa30-3010-9fd9-41ceb17f20f2 | -6.12794 | -41.76478 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a2e4101-a9a6-3105-b338-9ecd486c1fe6 | -4.92601 | -41.52067 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bbb94978-86b2-311a-ad18-e52fb39af72c | -9.2511 | -44.3631 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e509469b-8a88-3aee-8e8f-a6f4e5d7cdb2 | -6.68217 | -44.27847 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfef0d2a-bc84-3fa4-b24f-3e36f4241f36 | -9.13466 | -46.60083 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbc8b60c-5b5b-307b-8ddd-9f2faecea2ae | -5.39195 | -50.4823 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c86e92a2-7dc0-3e25-9d6d-1435c829bcfc | -5.16831 | -45.25215 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62c28241-e5ac-31f4-8952-0c1867b0e748 | -4.94543 | -44.44162 | 2025-10-17 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 870c99cb-7023-3402-b7fa-e4fc891f1bab | -6.58489 | -47.07165 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30e981b0-8e16-330e-bcec-bbde7fc3d049 | -9.1434 | -46.65386 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe3ad372-f06e-3b91-9657-43a856a6eb3d | -5.51818 | -47.0412 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22ca593c-9059-37cc-b666-140eead39fe3 | -9.0001 | -46.65315 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2ab1b63-ffca-3d03-994d-82188555cd0c | -8.2032 | -43.9687 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2946c7f7-abfd-3516-a797-2f55a9d7897a | -3.51381 | -50.21376 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc83dff8-cb0e-315d-9c65-3c48256e6737 | -6.68385 | -44.28936 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7593fad-3850-3edc-b817-dd1f879c2d0a | -6.22706 | -41.54276 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1c11bc7d-bbec-3ba9-9441-68ac40075e3c | -8.26319 | -44.08639 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa6735c6-2d42-3eb8-aa78-b7c1f5e7f953 | -5.81363 | -42.33812 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c9975d09-da2e-3ab4-8a4e-dbfd6b993b30 | -5.6853 | -48.96608 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c0dce8e-c952-3344-9aa7-cd4030a1be87 | -9.28832 | -46.91592 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ebeb39e-bf05-362a-893d-0c5832693bf5 | -8.40261 | -46.23751 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16fc12e6-3df1-3291-a3fe-5b5848c556db | -5.88374 | -44.7523 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84fe57c7-7475-3307-ad18-bde3bff05f51 | -6.34576 | -41.5004 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| afb4ba2e-0045-3ae4-b62d-16ebac9fdaa9 | -8.9871 | -45.36045 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f555ec3f-1192-37f9-8c17-a1f248962e5d | -5.50109 | -47.30295 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cb10aab-c6ef-3445-a34a-1f7d6110fb57 | -6.58898 | -47.06836 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1b8178a-d453-3b10-8587-24a508b9dd27 | -8.45606 | -46.24257 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70b8d1bc-22a3-352e-973d-0952d1684c14 | -11.2861 | -45.2793 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de558ef9-d0b6-3ac7-a091-ccbda073b288 | -4.26213 | -48.55039 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0277925-0179-3208-ad7e-634300c61cdc | -11.40937 | -44.20377 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 552fa8b1-55c9-3c80-8cb8-67b64590f4a2 | -6.46408 | -44.52311 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56b22843-7821-32f5-b8d2-24f3b4ff5baa | -7.27622 | -42.93887 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f0a58a57-c226-3744-a49d-1bd967fd5d32 | -9.71665 | -44.54111 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df851196-0a0d-3270-a683-c6ef77ddaedd | -10.05836 | -43.85968 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64f6e23a-1130-3006-97be-467b9bceb84b | -4.59171 | -46.33715 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1782bc9b-363b-37a1-bb48-5125d3f4a0dc | -6.35038 | -41.51825 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c0ad081-52ad-331d-ac06-51425db31a20 | -3.28652 | -52.59217 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ac85240-9ab1-3d42-9c0e-e49ef0830104 | -7.83492 | -45.46016 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1697f92e-01d9-3e66-93bf-889ba817ebd7 | -6.29566 | -45.52777 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c0261d0-b150-3dec-93b2-cece67994b80 | -4.8353 | -48.07645 | 2025-10-17 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56f4156e-1c32-359e-ba5f-f70e42a6898d | -4.4117 | -48.94965 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 921d6cae-ac32-32c0-9f86-ab962bad7adf | -10.58946 | -47.41418 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc40408-1497-3773-8510-e4df6db1ffba | -10.11903 | -44.6005 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b581b866-3d5c-38b6-9585-9231202cb85a | -6.14552 | -41.79229 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cde23076-9758-3994-9fa4-d7baf3709a8f | -6.289 | -42.97076 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README57.md)
