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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef7f511-16e3-3b20-b6e8-254612afd301 | -11.0556 | -45.76597 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a017b3c4-e128-3750-a3f5-54748893e2ca | -11.05177 | -45.71523 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 360.5 |
| ebef2c26-416a-383c-ac27-b403aa29d94c | -11.05015 | -45.72768 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 50c5fe93-3d2e-3a1f-9bd9-73b7e01b2be6 | -11.04852 | -45.74013 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| d356a9ca-75b1-3a4e-b625-5f472a22cf8e | -11.04143 | -45.71414 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 34bbc775-7de8-3193-a67f-aca4add85f9c | -11.03983 | -45.72651 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 49f4928a-3872-3624-be8a-1857f71384cb | -11.03823 | -45.73886 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| c5169d41-6526-3a06-9cc8-a57bf170e50c | -11.03451 | -45.70684 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f71e27e5-f443-3938-90ea-7da4020d220d | -11.03284 | -45.71918 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 0b27a1d7-caba-3199-83a5-8a7f5dfd2e1f | -11.03117 | -45.73149 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 1b8a134a-ee79-38a1-a546-25378c350065 | -11.03111 | -45.71288 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 12866275-b586-37af-89ed-723fecfb3f1d | -11.02952 | -45.72522 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| f2f9d380-cdf6-3025-bb19-ca190ea3dbd5 | -11.02421 | -45.70552 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 050f3a39-be69-3761-abc7-34b727d55c6d | -11.02254 | -45.71785 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 9e1d81a4-397d-30a5-8c6d-ad02be7e65c4 | -10.84362 | -45.98175 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 967e1826-4243-34de-b2ed-19fcbad203a5 | -10.8351 | -45.96853 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2ca8fcc4-8f0a-31ca-a04c-1e61188a5a1d | -10.82586 | -46.03865 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 00d6cfaf-76eb-3903-ad46-5ddaddb185b8 | -13.27427 | -46.33673 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| be407d50-2d3a-312b-ab7c-d76d1043c4c9 | -13.27268 | -46.34902 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| bc590512-104e-3109-9f3f-808f23a05992 | -13.26405 | -46.33556 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 19e76377-2515-3db0-9878-c3539c404818 | -13.26249 | -46.34771 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8cde05b7-b46d-363b-ab35-b498219eeacf | -13.24577 | -46.32866 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| dca595a9-8767-3cc6-9b64-f819a99ed4cc | -13.24503 | -46.32241 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ca11844d-2aac-370a-9945-70aa4ecf82ff | -13.24359 | -46.33364 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 85f689e9-3bb2-33d9-8e15-b0abe57b6e81 | -13.18115 | -45.45752 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 03b56c5d-5309-382e-91c2-22dfdc4ce9a9 | -13.17942 | -45.47145 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 280.7 |
| f749bd58-06a1-3743-bb64-d18661f3f288 | -13.17848 | -45.45133 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9600abdc-13e6-3085-8e5f-2260334c14f6 | -13.17665 | -45.46527 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 569.3 |
| 5dced200-9ffc-31f6-8bd9-d3c80d581199 | -13.1703 | -45.45616 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 5323f269-407c-3709-a5b6-9d0ea70a626c | -13.1686 | -45.46999 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 5ab5d128-77b6-3b58-842a-0cf5cbc00168 | -13.16763 | -45.44999 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 7d60afdf-7892-387f-b3c6-1e34b6739f07 | -13.16583 | -45.46382 | 2024-09-28 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0eeba3fd-3b37-37b5-a3ca-15e933a7960e | -12.75495 | -45.55235 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 08df8615-fc2f-31f6-b949-575d03e2e315 | -12.75322 | -45.56579 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.8 |
| 0b0014d2-998a-3645-a415-32904a0b81ea | -12.74425 | -45.55097 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7212fb4f-d0bf-359e-aab3-903e7b296160 | -12.74254 | -45.56435 | 2024-09-28 12:51:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9f563358-9981-3a6d-b2e1-c16040c1f105 | -14.26094 | -45.78325 | 2024-09-28 12:51:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 645d283c-4592-3c16-83f4-e44f558ba50b | -16.5724 | -46.84334 | 2024-09-28 12:51:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 848e52bd-baa2-302d-bf43-54ea9b322568 | -16.59024 | -46.92937 | 2024-09-28 12:51:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d93a558a-9dfa-31aa-aef0-c23c57899a2d | -16.58862 | -46.94232 | 2024-09-28 12:51:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 08988b04-4734-344f-8815-42b3b738510a | -16.57998 | -46.92812 | 2024-09-28 12:51:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a0ee0513-0bc6-3a79-a7ea-fc3717ccc764 | -15.41282 | -47.45397 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| eb47c039-76b2-389f-9808-2f15db2acadc | -9.25364 | -45.73982 | 2024-09-28 12:51:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 537a4c0b-fac2-3102-ac26-de69fd7b78e6 | -10.67933 | -46.06626 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| c9f0f44f-27cf-32ce-9153-612c2b938a8b | -10.67779 | -46.0777 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 93026031-45af-331e-862f-f3b6344fc863 | -10.67624 | -46.08911 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| c0797a75-30f1-3308-a04a-68f0ede80a95 | -10.67088 | -46.0534 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c0c17714-ad8f-355d-a8d8-b7400cdfa34e | -10.66934 | -46.06484 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 858.4 |
| 9d97eb5f-c9cc-3659-bedb-895df4ddbd8c | -10.6678 | -46.0763 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 617.0 |
| 84dfc5e2-765c-3198-817d-88b09feb5b8b | -10.66626 | -46.08776 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fcb6d6e0-6fda-3d84-9a41-f638f9a88785 | -10.66086 | -46.05209 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1037.5 |
| 0229a601-e6b4-3274-b101-9e49119e2e2b | -10.65933 | -46.06358 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1215.9 |
| 2d756e3f-d268-316d-af9d-dc0ccbc19558 | -10.65779 | -46.07508 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1468.0 |
| c74937c1-dc37-3aa2-9ad6-d878218e4feb | -10.65627 | -46.08648 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1702.1 |
| 928b34b0-cdd7-3b09-a004-7d3842f84faf | -10.65473 | -46.09793 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 49143651-2f6b-3a22-814a-fc291fa8b8bd | -10.65392 | -46.02766 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c2449102-562a-3378-bb8f-8015965b5825 | -10.65238 | -46.03927 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8b7063e1-eaa4-305d-89c5-fe3668aa6759 | -10.65085 | -46.0508 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 693.8 |
| d4fc3484-8fd9-32e8-ac7c-b8e0384a4c25 | -10.64932 | -46.06226 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 344fa825-b1a6-36b3-8def-5f4994987fbe | -10.6478 | -46.07369 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 127ce7cf-3239-3172-b683-ccf3dd09abff | -10.64628 | -46.08512 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 9bf9ab40-8540-342b-a3ab-52c865274e16 | -10.64474 | -46.09668 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bd1292d2-3832-3b89-bca0-b6c55d3695a7 | -10.64236 | -46.03795 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| fd9ac345-e0d0-3ffe-9a23-451b6628e0fe | -10.64084 | -46.04943 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bed06091-b170-30d8-b489-f0ea93c795ac | -10.63933 | -46.06086 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 338a96ae-fd30-3085-91a9-e8cbc8001695 | -10.63781 | -46.07231 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| fcd746f2-d3b9-3e9a-924f-2e1aeae30915 | -10.63629 | -46.08381 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 46cff63e-bd9b-3ba3-9027-3a49f3520f59 | -10.59845 | -46.06096 | 2024-09-28 12:51:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7e7f1d54-9e2e-3de8-bfbe-953ff3f7be5b | -10.58846 | -46.05962 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7db2e8d1-baf0-33ca-a82e-72dbb89361fd | -10.56002 | -46.04398 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7295622e-e878-3393-9839-8d4a9764b02e | -10.06793 | -46.06289 | 2024-09-28 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 317cfd3d-f39c-3100-9699-7b8b52cdbad7 | -10.06791 | -46.05661 | 2024-09-28 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| bc3b1638-179d-3adc-bb40-67acf1970e77 | -10.06638 | -46.0677 | 2024-09-28 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1ae52bd-46e6-3130-9b04-3ed397b6965e | -9.55626 | -46.52952 | 2024-09-28 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| be6157cb-7ad9-3385-b804-35832bb48bb2 | -9.54107 | -46.56982 | 2024-09-28 12:51:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c0c18454-8323-3da0-9020-4d820adc852a | -10.89807 | -46.41272 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 64dea2fd-e793-35a0-85b4-ea65d9569294 | -10.89122 | -46.38941 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f8878381-efa7-3155-9e6b-28222653d2b4 | -10.87307 | -46.37545 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 79386af8-b4d2-39ba-974e-0d8b2c27eea5 | -10.87158 | -46.38664 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 4c139f28-d3b2-3edf-bdd9-fceb01323040 | -10.86176 | -46.38525 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0f7a75ad-ab58-3e12-9264-ba2c1a3886b9 | -10.79604 | -46.56045 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 955c6f95-2d1d-30f5-9742-f4e4ebdaa4e5 | -10.79455 | -46.57133 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 283.5 |
| b44a2863-b3c5-30f0-a3ef-dc6d40f875a9 | -10.78481 | -46.57032 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3a00a545-1c6b-3952-8d0c-4e6d3db187ea | -10.41752 | -46.27261 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5dd5bd24-766e-3d2c-969e-3ab2de1e04ab | -10.41605 | -46.28367 | 2024-09-28 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 2b6de8f7-06a8-3eb4-ae24-db1ef4f24dd1 | -9.65069 | -45.82346 | 2024-09-28 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 86224f10-8c12-3435-862b-c6f2d449e39f | -11.87931 | -47.16582 | 2024-09-28 12:51:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8f78d85d-a97e-33ac-903e-c12d911156fe | -11.8712 | -47.15411 | 2024-09-28 12:51:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7620bf7d-9586-30f7-a8dc-a43d9b4b24d6 | -11.8698 | -47.16452 | 2024-09-28 12:51:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 4d8acab4-4f04-3a5a-a636-3e533823be65 | -11.79859 | -47.61966 | 2024-09-28 12:51:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08890027-8474-3097-9b2c-efd7b0dd42a6 | -11.7893 | -47.61839 | 2024-09-28 12:51:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0f5417ac-a5c0-392b-9c3b-a8417fe2660d | -11.70847 | -46.38276 | 2024-09-28 12:51:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 81fe9f4a-62b5-3209-b000-03aea1cd067b | -11.69455 | -46.33458 | 2024-09-28 12:51:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 81c45876-3417-3439-8c4a-1bbc62f6a728 | -11.4178 | -47.25023 | 2024-09-28 12:51:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b4bfda54-969f-3881-9e63-c35375c0a93d | -11.33205 | -46.88841 | 2024-09-28 12:51:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 52d2f65c-5194-3b1a-97d6-63869c8e19f7 | -12.97774 | -47.19659 | 2024-09-28 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dbc91935-9ff8-3d3d-97d4-6cfa8727b5d7 | -12.80673 | -47.4605 | 2024-09-28 12:51:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63760075-4f80-3a58-b5c0-8deba4c15091 | -16.02318 | -48.25293 | 2024-09-28 12:51:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4237bae7-e7bf-3933-bf31-4f79507f166e | -16.01846 | -48.2459 | 2024-09-28 12:51:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7edf6400-9f8f-3788-b5bb-79648d3cb85c | -15.79974 | -47.53024 | 2024-09-28 12:51:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 74.8 |


[Clique aqui para ver as próximas entradas](README104.md)
