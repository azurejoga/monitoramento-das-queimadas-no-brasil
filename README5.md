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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e53a1ca7-6931-3648-ac34-c7e71778118a | -17.51062 | -50.76332 | 2026-05-09 04:32:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34d35351-56f6-3496-a868-bf61bfd5e04c | -19.91287 | -44.047 | 2026-05-09 04:32:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd8f22e0-262f-3f4c-92f1-50405025d24f | -14.00392 | -56.63884 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c25cfb6-11bf-31f5-b70b-8aebeecd844a | -14.00623 | -56.62724 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31dc2a14-35b5-3a71-8148-d30ef3ef09ff | -16.76689 | -45.8178 | 2026-05-09 04:32:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 199e3eb6-3b08-343b-940c-88c247c205a2 | -18.60516 | -46.38291 | 2026-05-09 04:32:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1329f0c1-b6e5-332a-a5c5-f42751d0f4eb | -21.52905 | -47.13733 | 2026-05-09 04:32:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd3deab-b508-3d45-bce6-79324b2cece7 | -21.18315 | -45.87386 | 2026-05-09 04:32:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 39fcda0b-b609-3bd0-9327-13f7ff0d36ce | -20.23484 | -46.82789 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90c34cb7-ab36-3b87-a932-13b1bea8f412 | -18.29379 | -45.13091 | 2026-05-09 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60bb67b7-dd0b-383e-9b5a-30762c67dd7a | -18.92272 | -53.22118 | 2026-05-09 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3462165-cacf-3949-b97e-6130cd7425e1 | -17.94176 | -52.95422 | 2026-05-09 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 083f4fa6-cc79-3c97-b558-ac527d3b2d0c | -16.41147 | -54.92166 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5c0c6a-16d3-39bc-b06a-b7aa132728c0 | -16.44707 | -51.72197 | 2026-05-09 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5249dd65-9bae-3b5e-8851-baf66eeff29c | -11.78067 | -43.66491 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 813c3f57-2770-336d-adc2-3f0f4a0b61a5 | -11.77171 | -43.65422 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 443ab141-458b-378f-8bcc-f073d78107ca | -10.04705 | -51.67419 | 2026-05-09 04:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df5b73c7-d304-3744-af4a-4634da72cefc | -8.72653 | -48.32423 | 2026-05-09 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b0e524-75ca-3408-b357-976f3669bf58 | -9.45492 | -47.79184 | 2026-05-09 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b42da4f-3c9f-353a-9ee9-d14d16841e2f | -10.23833 | -52.22435 | 2026-05-09 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee3f81b7-6816-3ad3-a1bc-d40ec1363d6d | -8.69394 | -49.09452 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf362c83-6513-38e3-8ec9-aa2b07c2e009 | -11.76663 | -43.6535 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 873f0adb-0b2a-3678-8b9d-ec5a9204729a | -9.64314 | -42.96177 | 2026-05-09 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42584685-f5bb-37f2-9c1b-9e6ed153209e | -8.7267 | -47.97359 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be865f45-35fd-3e1f-a128-ace53bc6f285 | -11.77132 | -43.65728 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1411c9bf-a832-3afb-8cf1-c3ecbcfa8bf5 | -6.1867 | -44.86965 | 2026-05-09 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21410b69-9c9b-3f81-8cd1-ec3f3c22122b | -10.05091 | -51.67123 | 2026-05-09 04:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79cac2a4-afc2-3eee-a920-eba6929c6b57 | -10.64202 | -48.02029 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b593264f-7f34-3ec7-b4e9-355cf8ab1589 | -11.77679 | -43.65496 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ab68b29-7bba-3233-8d21-63ed9ae289ac | -9.64504 | -42.96016 | 2026-05-09 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aeab168c-55f1-3439-b038-5f6893086c48 | -5.78583 | -45.13239 | 2026-05-09 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75383216-f840-38db-beeb-7d6f0ce24808 | -10.66441 | -49.71437 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44741818-a5b2-32be-8229-906abc6e8380 | -10.67133 | -49.69184 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17fc56bf-0219-38d3-a3e6-c5b8f8a0a85f | -9.45425 | -47.79642 | 2026-05-09 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0d682c6-ab8d-3819-8b15-fff370ca074b | -8.68989 | -49.07407 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac2f82da-95c6-3b67-8654-3295e8fd56ff | -8.70149 | -49.09171 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd2aea02-8acf-3dae-a9a0-024b96646752 | -10.0476 | -51.67069 | 2026-05-09 04:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b73e6be-be6b-34e4-9320-245c23d5e982 | -8.72972 | -47.97849 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80bcbb93-4ff1-32e4-9caa-16a9e93800ad | -9.64464 | -42.96326 | 2026-05-09 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2f36008-6a35-3cb6-b699-34f786517ff1 | -11.42075 | -47.0924 | 2026-05-09 04:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d585756-1282-32c1-99e1-f00ca51e13c2 | -10.66614 | -49.70284 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 782b6ea4-2ac4-36f3-86b0-a0bd3ddab7a1 | -11.59826 | -47.10229 | 2026-05-09 04:49:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ccfe624-6d36-33d2-aaeb-bd930654c34f | -11.78107 | -43.66183 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b801ee1-d409-39c5-9420-52098f4ce81c | -8.70033 | -49.09944 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd068d8c-9a4a-3d37-82f6-cad06a88d6c5 | -8.72906 | -47.98279 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7317ecee-e9ef-3914-ac51-a6df6d83d01e | -8.70208 | -49.08784 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfbc6c8e-33a7-300b-b870-7b41c168697a | -11.7756 | -43.66417 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76b313e-a1c4-3089-9024-5dbfa220822c | -6.191 | -44.87035 | 2026-05-09 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20c226d5-a14a-3334-a117-be646c359ea6 | -6.3233 | -44.63804 | 2026-05-09 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92cb63fc-93c8-3486-9ebe-7bb210ae63f0 | -9.45774 | -47.82473 | 2026-05-09 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18462b74-d7e5-3b3a-98d9-56aabf482723 | -8.70324 | -49.0801 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6532f91-fc9d-3270-a142-6bd5aafae06a | -11.93978 | -43.38329 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0242d623-1f64-3a1b-9b37-8232a79736ed | -10.63072 | -48.01889 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff1e51e9-fa1f-3489-9379-1ac29cfb2271 | -11.776 | -43.66107 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 694247fb-4562-383c-98ce-687d429c0b6c | -11.94147 | -43.3799 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b1a8ed0-e716-3b56-a148-b02f92d77ef1 | -6.32889 | -44.63036 | 2026-05-09 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f9309fd-b2f9-3643-886d-0806959d2c95 | -10.72943 | -43.98626 | 2026-05-09 04:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f6bcd16-1219-3141-923b-aa86600b051a | -8.72949 | -47.97629 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6b46364-082a-39ea-bf36-765a0231e290 | -11.76634 | -44.09157 | 2026-05-09 04:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 201c78f3-87a8-30cb-a63b-d5531b354973 | -10.55172 | -42.43808 | 2026-05-09 04:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f852f4b6-216a-3695-a6f7-643c6163bb6f | -5.78278 | -45.12408 | 2026-05-09 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80515870-e71b-3198-bf22-938264e8f3ee | -8.72605 | -47.97792 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfb1439d-cfd3-31de-9ba6-95da4704a9d9 | -11.77211 | -43.65116 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6032fabc-d69f-3406-acd8-9c9c4c0f4900 | -8.72292 | -48.32366 | 2026-05-09 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dc08014-70fe-3a23-aee6-1e8ee3d64086 | -9.30439 | -48.58631 | 2026-05-09 04:49:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f29d737c-d236-3410-b216-724ad4cf57f4 | -5.78526 | -45.13617 | 2026-05-09 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7858fae7-3ada-3f81-9bd9-2d7aed0f8b51 | -10.6696 | -49.70337 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f95099ab-918b-3f14-a14a-35a409713bb1 | -5.7864 | -45.12861 | 2026-05-09 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ac755b-5214-3e61-8fe5-733a730261d2 | -10.66844 | -49.68745 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc52bc4-c667-3c74-a9d7-fb471e4377bc | -10.64137 | -48.02474 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d46e1925-11ec-3797-8b5e-3a4761f586b3 | -10.66268 | -49.7023 | 2026-05-09 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28317042-d723-3b6a-a7f7-15260fbeff1d | -11.77639 | -43.65802 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0d93860-1133-3643-a452-d806bcfe4616 | -11.94018 | -43.38018 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab3e4cef-5611-37fe-9dcb-33d2a9837e6d | -10.55218 | -42.43454 | 2026-05-09 04:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f14863b1-bedf-3fc7-9d26-815b6eac0e0f | -10.6314 | -48.0143 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcd0f04a-12ec-3947-9283-cb131e5050c2 | -8.70381 | -49.09995 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e43c077-d1b7-3cc3-9dd9-f8cf23037317 | -9.44554 | -46.12292 | 2026-05-09 04:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b5e8af-6ced-3836-a50d-b0230a0c32b3 | -11.77719 | -43.6519 | 2026-05-09 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6a737b1-181a-349f-a3f2-da517649e0ff | -8.72539 | -47.98223 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc85dca1-d6a2-3943-8e34-314d340007f1 | -10.63579 | -48.0105 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8171052-4a18-3041-87dc-6456eb412abb | -9.305 | -48.58219 | 2026-05-09 04:49:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3ed2adc-18ce-3d0d-99aa-a84cc68f6346 | -8.70266 | -49.08398 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 406390ed-5056-3ad2-9b73-9992fb926bb1 | -11.94183 | -43.37696 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e21a6894-78fb-31af-9c70-336ed54e39f8 | -9.64384 | -42.96953 | 2026-05-09 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 442ce232-4784-3040-ba65-6f1f59fcb9e2 | -10.63514 | -48.01493 | 2026-05-09 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b369ad4d-dc5c-3aef-8af6-36fa0d2d0965 | -11.94057 | -43.37721 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef57067a-296f-3f4f-af50-723c68eb5b69 | -9.64343 | -42.97268 | 2026-05-09 04:49:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 503a1c94-ce3d-3013-aaef-2e852259adfc | -8.72823 | -47.98492 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ea2b954-d9cf-36cf-ad7b-1675ca59e379 | -11.77622 | -44.0929 | 2026-05-09 04:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c60fb73-760d-366d-81d6-1ada390ce7b0 | -11.94109 | -43.383 | 2026-05-09 04:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a58aca3b-8513-319f-b945-b003bccf7ef2 | -8.72528 | -48.3326 | 2026-05-09 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b5d6618-8eaf-3da7-8835-c2cf3d7786a1 | -10.04815 | -51.6672 | 2026-05-09 04:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec88ec9-c3ce-3a55-b221-78abdc781bb2 | -8.70323 | -49.10381 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb49e442-2939-327a-adfd-4049e9925cfa | -6.22303 | -55.64304 | 2026-05-09 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0d3bfd8-2083-37c1-b608-46b912ce87e8 | -8.69047 | -49.07019 | 2026-05-09 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4f2b193-1c9f-35d1-94d0-80a0d488fe76 | -11.42125 | -47.08886 | 2026-05-09 04:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 967d3ddd-6c59-3075-9621-13025e5e135e | -11.06523 | -49.47103 | 2026-05-09 04:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e5761f3-f8a9-3056-9ea8-f31ede78a850 | -11.7755 | -44.09854 | 2026-05-09 04:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 698f173f-be53-3047-b35b-66b734270693 | -8.72886 | -47.98061 | 2026-05-09 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 839cbd9e-5d67-3c9f-8c18-60ff2f99ba02 | -12.7804 | -47.42682 | 2026-05-09 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README6.md)
