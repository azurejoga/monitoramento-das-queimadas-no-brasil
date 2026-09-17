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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1229675-974b-3154-a44b-38c14c068d67 | -12.49903 | -50.83228 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ed750f9e-df1b-3331-a1ce-777e41fb7e20 | -7.46153 | -42.10826 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2dfebece-659d-32ff-b751-21d42c20c2a6 | -7.4593 | -42.1077 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b22adfa-a484-3b8b-a026-ca35b4d6bf20 | -7.18193 | -41.80255 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 594858d9-a83a-3198-8c02-9e8de98dbe01 | -8.86498 | -45.88432 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 935e0ede-407a-3ba8-a718-23cf68bd812c | -7.36888 | -44.48248 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 983de63f-4f3b-33f7-ba31-b09ea4b969d4 | -7.11464 | -42.08784 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4d14478-d754-3008-9ce0-cf48955a48d8 | -6.7934 | -43.17178 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7cebbe7-89b5-3813-ab01-8522bd385e87 | -8.56315 | -44.54471 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58096535-3a0c-3b27-ad97-0937cc5061c0 | -8.49984 | -44.91085 | 2026-09-17 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ba34557-371f-3430-b730-e69c3291ff11 | -11.56978 | -46.86972 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 803cf606-a0f3-3f56-9070-d29ddaff13c3 | -8.26029 | -42.1586 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 28e9447a-540e-3e07-a78d-1d972ecb5949 | -12.14706 | -48.26078 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c113442f-894f-336d-9672-73bfca6ccaff | -7.57556 | -46.339 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a9b7ed0-e620-3731-894d-9caf63de3616 | -14.55614 | -39.63599 | 2026-09-17 03:55:00 | NOAA-20 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0f0768c-981f-338b-a033-e1a80db01133 | -12.47568 | -50.81569 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f7db1629-03b9-35bb-ba8d-3696f1f63078 | -12.46028 | -50.78959 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 7a23aeff-f5e2-3d83-bab7-d247d4b95fc3 | -9.95779 | -45.3257 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b705620-c88e-304c-87db-8b68ca6c1d07 | -8.56016 | -44.47708 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b695b57e-b752-3ca9-8416-530808e29183 | -11.98177 | -52.46434 | 2026-09-17 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccdf8074-cdee-3ce5-ace2-ee0a1efd3abc | -9.87215 | -48.38992 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 216aed43-2040-3860-a3e0-feb2bc4e2e24 | -12.46978 | -50.94086 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ca74266-1aaf-34ae-aca1-089163c6b900 | -7.81059 | -44.85912 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5285ae30-ca92-36d9-91cb-bdc5bbffe03b | -9.94938 | -45.29162 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64d77ea7-52bb-3d97-88de-923b0cbde32d | -7.142 | -42.15359 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 056121f8-45a1-328b-9acf-1174848faeb2 | -7.03448 | -42.0745 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 250c1ac5-7983-385f-b0a9-ed678ee53be3 | -9.48656 | -45.42784 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4099f8b-ab11-3ded-99d8-a6c2585a9b02 | -7.12526 | -42.17314 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b2689ee5-a565-33bb-8862-cf0f260274aa | -7.07748 | -41.77736 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 485e48e2-d501-34fc-b4d5-0b19efc37699 | -12.45561 | -50.84563 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 4dabe380-4bf5-3a14-ba54-3ad4d2707c24 | -9.10775 | -45.73416 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a34450e-fe17-3879-a6dc-e81c4e7ee56c | -9.11048 | -45.72521 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b03afb13-90e7-30ec-a686-b357eb4082fb | -11.53351 | -46.86562 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df5ba3a6-08de-396b-89d8-675699e637fa | -12.46035 | -50.92134 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea260827-34fe-39aa-9ad1-4e07863145b0 | -7.96549 | -43.97194 | 2026-09-17 03:55:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c29c034d-c5c2-34f2-940c-3c71cacc8c9e | -8.56014 | -44.55581 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 716f5030-f99e-3e40-aed0-b0bbc1ff9885 | -12.45487 | -50.85103 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 108dd843-b1d8-39b8-8814-9617535d9603 | -7.35477 | -44.4804 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fd544d3-a22c-3fd3-b9ad-f7f337fa6721 | -9.1144 | -45.73163 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 8b6ad221-7060-38c7-8270-70770a76f380 | -9.82175 | -46.50003 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58a8b64c-b8b5-39eb-abd5-39f0a6a5a51b | -7.02974 | -42.07032 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e188e0d9-526f-3757-85a9-08b1545146e6 | -11.63761 | -47.34023 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b810ed0-c50b-320d-842d-30111478dffe | -9.59274 | -46.64892 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ddb0119-7efd-3fe4-b02e-88ee0ce4d895 | -11.34732 | -43.97001 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bae41f48-0007-39ef-8418-c0b1fd5278c8 | -7.04614 | -42.05463 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd66489f-c635-37cc-96f5-f06c40bc3a28 | -6.88892 | -43.74418 | 2026-09-17 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 862773d8-3cf6-3b42-81b2-2d510968bfed | -7.17224 | -42.09744 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f3a928b-c8f6-3915-8f42-0d31fcfa7c59 | -10.37483 | -46.89365 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23c5fdcf-b716-3ca7-b69d-1335ba9e1fd3 | -11.36103 | -41.38682 | 2026-09-17 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e96835a1-6f3d-3f0a-9971-fd7b5b96e40c | -7.0662 | -42.13045 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bf21bf4d-69f6-3be6-9c06-4fcd3bedea91 | -8.56071 | -44.5588 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc9dd559-5a52-3c64-a3f9-f12d7fc2d41b | -12.46129 | -50.85245 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b976dc60-4a16-34de-89cd-08d496993059 | -9.60534 | -45.33957 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9658b675-ddae-3003-89c3-e0f632a4a35a | -7.37935 | -44.51743 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48dae3c9-f80d-3f69-93d3-74416ece671f | -12.4387 | -50.9281 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2676c68b-a393-30f9-8e09-685d29dc4041 | -9.82011 | -46.49825 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c296d108-b76e-33d0-bc62-adb4b003b1f8 | -7.12241 | -42.16535 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 495f3049-2068-350a-9d43-0b96c2089945 | -10.50367 | -46.3367 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7484ba4-44db-3c14-ae06-8ea50b50b56c | -8.58163 | -44.56863 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87228c95-034c-3b4e-b1a7-c811b4e06c5e | -9.46566 | -45.45395 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e91bb1d-9f1c-3709-a1e5-2ab6c1c5b947 | -12.47526 | -50.84985 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 064911f0-d7dc-3ba6-85d4-75899cc2e872 | -7.14078 | -42.16069 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2c10ce6-1a37-3cd9-b311-e5ceedaad2e9 | -8.5871 | -44.56462 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08d40aeb-be89-362f-9552-d59495a59ef4 | -12.45876 | -50.80054 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a4d6c414-3401-3d11-bb6b-c7a2505dc777 | -9.60058 | -45.33863 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e9eab223-ccc9-3ead-aa65-0a30e0942624 | -12.43883 | -50.92837 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b02cb7ef-3432-3163-a754-94e73eb5ee96 | -11.47757 | -45.77257 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee956609-1b7f-3f9f-9f01-db9ccbe3beed | -11.12915 | -49.0444 | 2026-09-17 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab3f4669-9b2f-3660-9f75-c6d9a715aec6 | -12.43497 | -50.81804 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16671460-cbad-39df-a85d-ee3d36c32fdc | -6.44723 | -46.53033 | 2026-09-17 03:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae323e2e-30d5-33a8-ad25-2ec53a14154b | -12.47553 | -50.91317 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a65b1fb-d3b0-3bd9-8bda-77907d3db096 | -9.87366 | -48.38196 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e1176c4-b55e-35a7-a872-eddb92ad68aa | -12.45005 | -50.87307 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54c278d5-c5a2-364b-966c-afc8193337d4 | -12.14156 | -48.25955 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fe848e0-9346-3904-a9bf-bb2233e9a4e2 | -8.47866 | -44.70007 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed206340-f0d4-3aed-b0fb-1036ed20d5bf | -14.13329 | -44.00866 | 2026-09-17 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33914595-5286-352e-b01b-1dcaf300b5e9 | -9.59353 | -46.64697 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3617e935-24af-32be-98e1-6b120c3f99b4 | -10.04288 | -45.56109 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5d8614c-e64b-3eeb-aae5-04b9f3b20ffb | -10.53903 | -44.85563 | 2026-09-17 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef6e6ff7-31c4-31ad-bebf-5a64b9f282d3 | -11.889 | -47.58773 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fb4cf9a4-3a05-319f-94a5-27cd2a5cc92b | -12.37471 | -48.46905 | 2026-09-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e5cd0b0-8b5a-38f6-a47f-5edaf74a28a8 | -7.10756 | -43.10744 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a99ef766-f001-3727-b211-dc770fb1bc99 | -7.04672 | -42.05122 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2932117a-7170-37e9-9523-a726a87ddf2a | -13.43193 | -43.81275 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d8cb7e05-eb8d-330d-a332-f5949b45face | -9.11151 | -45.71962 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 51de897e-16c3-3260-a66c-542ae5eecddb | -9.75515 | -46.11712 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba848a91-1e01-3977-aca8-ac6426eb3e14 | -13.43532 | -43.81714 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fc730ea4-1fb1-3108-9677-d60731c85370 | -9.95177 | -45.30122 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d917726-ad7b-3426-bf7f-fea2c05d796e | -12.46515 | -50.80196 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 449eb96c-5bc2-3e60-a8f3-62963970997a | -12.4691 | -50.91173 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78ff1738-5020-3f8a-b10c-136a0bce29b5 | -8.90582 | -43.8904 | 2026-09-17 03:55:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a6e4b60-344b-3ce5-abc1-6f74fd87b4ec | -13.60794 | -46.95508 | 2026-09-17 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82b774c4-3059-3b96-be48-d35ed4663bd1 | -12.45602 | -50.84557 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbc502d6-f879-3f0e-bf61-6c3b85cb4614 | -12.46014 | -50.85793 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57c7769b-747d-32c6-8550-85a3f0792567 | -7.30389 | -42.35401 | 2026-09-17 03:55:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce053fc0-71bc-378f-b702-da3a55cc02cb | -12.31362 | -47.96133 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2039fc76-e20c-3ca4-9377-58dc3b654406 | -9.62423 | -45.37105 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 9cec1477-1a55-3897-9c91-89639c049dd5 | -8.39659 | -42.21091 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 46872c37-a9e7-34d9-b4ff-db5bb9b7f2b4 | -9.10577 | -45.71658 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d2182860-6740-3f34-bfc1-7ce9956aac96 | -11.57136 | -46.88955 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
